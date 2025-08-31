"""
API routes for providing data endpoints.
"""
from fastapi import APIRouter, HTTPException
from typing import List, Optional
from app.models.portfolio import Project, Article, ContactInfo
from app.services.portfolio_service import portfolio_service

router = APIRouter(prefix="/api", tags=["api"])


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": "Portfolio API is running"}


@router.get("/contact", response_model=ContactInfo)
async def get_contact_info():
    """Get contact information."""
    return portfolio_service.contact_info


@router.get("/projects", response_model=List[Project])
async def get_projects(category: Optional[str] = None, featured: Optional[bool] = None):
    """Get projects with optional filtering."""
    projects = portfolio_service.projects
    
    if category:
        projects = [p for p in projects if p.category.lower() == category.lower()]
    
    if featured is not None:
        projects = [p for p in projects if p.featured == featured]
    
    return projects


@router.get("/projects/{project_id}", response_model=Project)
async def get_project(project_id: str):
    """Get a specific project by ID."""
    project = portfolio_service.get_project_by_id(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.get("/articles", response_model=List[Article])
async def get_articles(category: Optional[str] = None, featured: Optional[bool] = None):
    """Get articles with optional filtering."""
    articles = portfolio_service.articles
    
    if category:
        articles = [a for a in articles if a.category.lower() == category.lower()]
    
    if featured is not None:
        articles = [a for a in articles if a.featured == featured]
    
    return articles


@router.get("/articles/{article_id}", response_model=Article)
async def get_article(article_id: str):
    """Get a specific article by ID."""
    article = portfolio_service.get_article_by_id(article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@router.get("/tech-stack")
async def get_tech_stack(category: Optional[str] = None):
    """Get technology stack with optional category filtering."""
    tech_stack = portfolio_service.tech_stack
    
    if category:
        tech_stack = portfolio_service.get_tech_by_category(category)
    
    return tech_stack
