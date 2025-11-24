from fastapi import APIRouter, Request, HTTPException, Depends, status, Form, Response
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import List, Optional
import json
import os
import uuid
from datetime import datetime, timedelta
import re
from pathlib import Path
from jose import JWTError, jwt
import pyotp

from app.core.config import settings
from app.services.portfolio_service import portfolio_service
from app.core import security

import subprocess
import shutil

router = APIRouter()
templates = Jinja2Templates(directory=settings.template_dir)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="admin/login")

async def get_current_admin(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        # If it's a page request, return None to let the caller handle redirect
        # If it's an API request (like fetch-medium), raise 401
        if request.url.path == "/admin/add-article" or \
           request.url.path == "/admin/manage-articles":
            return None
            
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    try:
        # Remove "Bearer " prefix if present
        if token.startswith("Bearer "):
            token = token.split(" ")[1]
            
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        username: str = payload.get("sub")
        if username is None or username != settings.admin_username:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    except Exception as e:
        print(f"Error decoding token: {e}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token validation failed")
    
    return username

# Middleware-like dependency for HTML pages
async def admin_required(request: Request):
    try:
        user = await get_current_admin(request)
        if user is None:
            return False
    except HTTPException:
        return False
    return True

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("admin/login.html", {
        "request": request,
        "app_name": settings.app_name,
        "page_title": "Admin Login",
        "contact_email": settings.contact_email,
        "linkedin_url": settings.linkedin_url,
        "github_url": settings.github_url,
        "twitter_url": settings.twitter_url,
        "medium_url": settings.medium_url,
        "portfolio": portfolio_service.get_portfolio_data()
    })

@router.post("/login")
async def login(
    response: Response,
    username: str = Form(...),
    password: str = Form(...),
    totp_code: str = Form(...)
):
    # 1. Verify Username & Password
    if username != settings.admin_username or password != settings.admin_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    
    # 2. Verify TOTP
    totp = pyotp.TOTP(settings.admin_totp_secret)
    if not totp.verify(totp_code):
        # Allow a small window or check if it's a valid code
        # For development/testing, you might want to print the current code
        # print(f"Current TOTP: {totp.now()}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid 2FA code",
        )
    
    # 3. Create Token
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = security.create_access_token(
        data={"sub": username}, expires_delta=access_token_expires
    )
    
    # 4. Set Cookie
    response.set_cookie(
        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True,
        max_age=settings.access_token_expire_minutes * 60,
        path="/",
        samesite="lax",
        secure=False  # Set to True in production with HTTPS
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/logout")
async def logout():
    response = RedirectResponse(url="/admin/login", status_code=303)
    response.delete_cookie(
        key="access_token",
        path="/",
        samesite="lax"
    )
    return response

class MediumRequest(BaseModel):
    url: str

class ArticleData(BaseModel):
    id: str
    title: str
    excerpt: str
    category: str
    tags: List[str]
    published_date: str
    read_time: int
    featured: bool
    image_url: Optional[str] = None
    external_url: Optional[str] = None

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def get_medium_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    
    # Try urllib first
    try:
        import urllib.request
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Urllib failed: {e}")
        
        # Try curl if available (fallback for 403s)
        if shutil.which("curl"):
            try:
                result = subprocess.run(
                    ["curl", "-L", "-A", headers['User-Agent'], url],
                    capture_output=True,
                    text=True,
                    encoding='utf-8',
                    errors='ignore'
                )
                if result.returncode == 0 and result.stdout:
                    return result.stdout
            except Exception as curl_e:
                print(f"Curl failed: {curl_e}")
                
        raise e

@router.get("/add-article", response_class=HTMLResponse)
async def add_article_page(request: Request):
    # Check authentication first
    if not await admin_required(request):
        return RedirectResponse(url="/admin/login", status_code=303)

    try:
        # Load metadata for dropdowns
        try:
            with open('data/blog_metadata.json', 'r', encoding='utf-8') as f:
                metadata = json.load(f)
        except FileNotFoundError:
            metadata = {"categories": [], "tags": []}
        
        # Build context similar to pages.py
        context = {
            "request": request,
            "categories": metadata.get("categories", []),
            "tags": metadata.get("tags", []),
            "app_name": settings.app_name,
            "contact_email": settings.contact_email,
            "linkedin_url": settings.linkedin_url,
            "github_url": settings.github_url,
            "twitter_url": settings.twitter_url,
            "medium_url": settings.medium_url,
            "portfolio": portfolio_service.get_portfolio_data()
        }
            
        return templates.TemplateResponse("admin/add_article.html", context)
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.post("/fetch-medium")
async def fetch_medium(data: MediumRequest, username: str = Depends(get_current_admin)):
    try:
        from html.parser import HTMLParser

        class MetaParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.meta = {}
            def handle_starttag(self, tag, attrs):
                if tag == 'meta':
                    attrs_dict = dict(attrs)
                    if 'property' in attrs_dict:
                        prop = attrs_dict['property']
                        if prop.startswith('og:'):
                            self.meta[prop] = attrs_dict.get('content')
                    elif 'name' in attrs_dict:
                        name = attrs_dict['name']
                        if name == 'description':
                            self.meta['description'] = attrs_dict.get('content')
                        elif name == 'twitter:data1':
                            self.meta['twitter:data1'] = attrs_dict.get('content')
                        elif name == 'article:published_time':
                            self.meta['article:published_time'] = attrs_dict.get('content')

        # Get HTML using robust method
        html = get_medium_html(data.url)
            
        parser = MetaParser()
        parser.feed(html)
        
        # Extract read time (heuristic or from meta)
        read_time = 5 # Default
        
        # Extract published date
        published_date = parser.meta.get('article:published_time')
        
        # Try to parse Apollo State for better data
        apollo_match = re.search(r'window\.__APOLLO_STATE__\s*=\s*({.+?})</script>', html)
        if apollo_match:
            try:
                apollo_data = json.loads(apollo_match.group(1))
                
                # Try to find the post
                post = None
                
                # 1. Try to extract ID from URL
                post_id = None
                url_match = re.search(r'-([a-f0-9]+)$', data.url)
                if url_match:
                    post_id = url_match.group(1)
                    post = apollo_data.get(f"Post:{post_id}")
                
                # 2. If not found, look for any Post with matching title
                if not post:
                    title = parser.meta.get('og:title', '')
                    for key, value in apollo_data.items():
                        if key.startswith('Post:') and value.get('title') == title:
                            post = value
                            break
                
                if post:
                    if 'readingTime' in post:
                        read_time = int(round(post['readingTime']))
                    
                    if 'firstPublishedAt' in post and post['firstPublishedAt']:
                        dt = datetime.fromtimestamp(post['firstPublishedAt'] / 1000)
                        published_date = dt.isoformat()
                    elif 'updatedAt' in post and post['updatedAt']:
                        dt = datetime.fromtimestamp(post['updatedAt'] / 1000)
                        published_date = dt.isoformat()
                        
            except Exception as e:
                print(f"Apollo parse error: {e}")

        # Fallback for read time if not found in Apollo
        if read_time == 5:
            twitter_data1 = parser.meta.get('twitter:data1')
            if twitter_data1 and 'min read' in twitter_data1:
                 try:
                     read_time = int(twitter_data1.split()[0])
                 except:
                     pass
        
        # Fallback for date
        if not published_date:
             published_date = datetime.now().isoformat()

        return {
            "title": parser.meta.get('og:title', ''),
            "description": parser.meta.get('og:description', '') or parser.meta.get('description', ''),
            "image": parser.meta.get('og:image', ''),
            "url": parser.meta.get('og:url', data.url),
            "read_time": read_time,
            "published_date": published_date
        }
        
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})

@router.post("/save-article")
async def save_article(article: ArticleData, username: str = Depends(get_current_admin)):
    try:
        # Parse date
        pub_date = datetime.fromisoformat(article.published_date)
        year = str(pub_date.year)
        month = f"{pub_date.month:02d}"
        
        # Create directory
        cat_slug = slugify(article.category)
        base_dir = Path(settings.data_dir) / "articles" / cat_slug / year / month
        base_dir.mkdir(parents=True, exist_ok=True)
        
        # File path
        file_path = base_dir / f"{article.id}.json"
        
        # Prepare data with UUID and Slug
        data = article.dict()
        data['primary_id'] = str(uuid.uuid4())
        data['slug'] = article.id # Use ID as slug
        
        # Save JSON
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            
        # Update metadata if new tags/categories
        meta_path = Path('data/blog_metadata.json')
        if meta_path.exists():
            with open(meta_path, 'r', encoding='utf-8') as f:
                meta = json.load(f)
            
            updated = False
            if article.category not in meta['categories']:
                meta['categories'].append(article.category)
                meta['categories'].sort()
                updated = True
                
            for tag in article.tags:
                if tag not in meta['tags']:
                    meta['tags'].append(tag)
                    updated = True
            
            if updated:
                meta['tags'].sort()
                with open(meta_path, 'w', encoding='utf-8') as f:
                    json.dump(meta, f, indent=4)
        
        # Refresh the portfolio service cache
        portfolio_service.refresh_data()
                    
        return {"success": True, "path": str(file_path)}
        
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "message": str(e)})
    
@router.get("/manage-articles", response_class=HTMLResponse)
async def manage_articles_page(request: Request):
    # Check authentication first
    if not await admin_required(request):
        return RedirectResponse(url="/admin/login", status_code=303)

    context = {
        "request": request,
        "articles": portfolio_service.get_portfolio_data().articles,
        "app_name": settings.app_name,
        "contact_email": settings.contact_email,
        "linkedin_url": settings.linkedin_url,
        "github_url": settings.github_url,
        "twitter_url": settings.twitter_url,
        "medium_url": settings.medium_url,
        "portfolio": portfolio_service.get_portfolio_data()
    }
    return templates.TemplateResponse("admin/manage_articles.html", context)

@router.delete("/delete-article/{article_id}")
async def delete_article(article_id: str, username: str = Depends(get_current_admin)):
    try:
        # Find the article to get its path details
        article = portfolio_service.get_article_by_id(article_id)
        if not article:
            return JSONResponse(status_code=404, content={"success": False, "message": "Article not found"})
            
        # Reconstruct file path
        cat_slug = slugify(article.category)
        year = str(article.published_date.year)
        month = f"{article.published_date.month:02d}"
        
        file_path = Path(settings.data_dir) / "articles" / cat_slug / year / month / f"{article.id}.json"
        
        if file_path.exists():
            os.remove(file_path)
            
            # Clean up empty directories if any
            try:
                # Try to remove month dir if empty
                if not any(file_path.parent.iterdir()):
                    file_path.parent.rmdir()
                    # Try to remove year dir if empty
                    if not any(file_path.parent.parent.iterdir()):
                        file_path.parent.parent.rmdir()
            except Exception:
                pass # Ignore directory cleanup errors
                
            # Refresh cache
            portfolio_service.refresh_data()
            return {"success": True, "message": "Article deleted successfully"}
        else:
            # If file not found but exists in cache, force refresh
            portfolio_service.refresh_data()
            return JSONResponse(status_code=404, content={"success": False, "message": "Article file not found"})
            
    except Exception as e:
        import traceback
        print(f"Error deleting article {article_id}:")
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"success": False, "message": f"Internal Error: {str(e)}"})
