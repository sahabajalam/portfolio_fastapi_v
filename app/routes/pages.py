"""
Page routes for serving HTML pages.
"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.core.templates import template_manager
from app.services.portfolio_service import portfolio_service

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
@router.get("/index.html", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the home page with portfolio data."""
    portfolio_data = portfolio_service.get_portfolio_data()
    featured_projects = portfolio_service.get_featured_projects(limit=3)
    featured_articles = portfolio_service.get_featured_articles(limit=2)
    
    context = {
        "request": request,
        "portfolio": portfolio_data,
        "featured_projects": featured_projects,
        "featured_articles": featured_articles,
        "page_title": "Home"
    }
    
    return template_manager.render("pages/index.html", context)


@router.get("/projects", response_class=HTMLResponse)
@router.get("/projects.html", response_class=HTMLResponse)
async def projects(request: Request):
    """Serve the projects page."""
    portfolio_data = portfolio_service.get_portfolio_data()
    
    context = {
        "request": request,
        "portfolio": portfolio_data,
        "projects": portfolio_data.projects,
        "page_title": "Projects"
    }
    
    return template_manager.render("pages/projects.html", context)


@router.get("/articles", response_class=HTMLResponse)
@router.get("/articles.html", response_class=HTMLResponse)
async def articles(request: Request):
    """Serve the articles page."""
    portfolio_data = portfolio_service.get_portfolio_data()
    
    context = {
        "request": request,
        "portfolio": portfolio_data,
        "articles": portfolio_data.articles,
        "page_title": "Articles"
    }
    
    return template_manager.render("pages/articles.html", context)


@router.get("/all-articles", response_class=HTMLResponse)
@router.get("/all-articles.html", response_class=HTMLResponse)
async def all_articles(request: Request):
    """Serve the all articles page with filtering and pagination."""
    portfolio_data = portfolio_service.get_portfolio_data()
    
    context = {
        "request": request,
        "portfolio": portfolio_data,
        "articles": portfolio_data.articles,
        "page_title": "All Articles"
    }
    
    return template_manager.render("pages/all_articles.html", context)
