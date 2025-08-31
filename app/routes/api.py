"""
Optimized API routes with consolidated filtering logic.
"""
from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional, TypeVar, Generic
from app.models.portfolio import Project, Article, ContactInfo
from app.services.portfolio_service import portfolio_service

router = APIRouter(prefix="/api", tags=["api"])

T = TypeVar('T', Project, Article)


class FilterService:
    """Centralized filtering service to eliminate code duplication."""
    
    @staticmethod
    def filter_items(
        items: List[T], 
        category: Optional[str] = None, 
        featured: Optional[bool] = None
    ) -> List[T]:
        """Generic filtering logic for projects and articles."""
        filtered_items = items
        
        if category:
            filtered_items = [
                item for item in filtered_items 
                if item.category.lower() == category.lower()
            ]
        
        if featured is not None:
            filtered_items = [
                item for item in filtered_items 
                if item.featured == featured
            ]
        
        return filtered_items


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": "Portfolio API is running"}


@router.get("/contact", response_model=ContactInfo)
async def get_contact_info():
    """Get contact information."""
    return portfolio_service.contact_info


@router.get("/projects", response_model=List[Project])
async def get_projects(
    category: Optional[str] = Query(None, description="Filter by category"),
    featured: Optional[bool] = Query(None, description="Filter by featured status"),
    limit: Optional[int] = Query(None, ge=1, description="Limit number of results")
):
    """Get projects with optional filtering and limiting."""
    projects = FilterService.filter_items(
        portfolio_service.projects, 
        category=category, 
        featured=featured
    )
    
    return projects[:limit] if limit else projects


@router.get("/projects/{project_id}", response_model=Project)
async def get_project(project_id: str):
    """Get a specific project by ID."""
    project = portfolio_service.get_project_by_id(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.get("/articles", response_model=List[Article])
async def get_articles(
    category: Optional[str] = Query(None, description="Filter by category"),
    featured: Optional[bool] = Query(None, description="Filter by featured status"),
    limit: Optional[int] = Query(None, ge=1, description="Limit number of results")
):
    """Get articles with optional filtering and limiting."""
    articles = FilterService.filter_items(
        portfolio_service.articles, 
        category=category, 
        featured=featured
    )
    
    return articles[:limit] if limit else articles


@router.get("/articles/{article_id}", response_model=Article)
async def get_article(article_id: str):
    """Get a specific article by ID."""
    article = portfolio_service.get_article_by_id(article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@router.get("/tech-stack")
async def get_tech_stack(
    category: Optional[str] = Query(None, description="Filter by category"),
    limit: Optional[int] = Query(None, ge=1, description="Limit number of results")
):
    """Get technology stack with optional category filtering."""
    tech_stack = portfolio_service.tech_stack
    
    if category:
        tech_stack = portfolio_service.get_tech_by_category(category)
    
    return tech_stack[:limit] if limit else tech_stack


@router.get("/featured")
async def get_featured_content(
    projects_limit: int = Query(3, ge=1, description="Number of featured projects"),
    articles_limit: int = Query(2, ge=1, description="Number of featured articles")
):
    """Get featured content (projects and articles) in one request."""
    return {
        "projects": portfolio_service.get_featured_projects(limit=projects_limit),
        "articles": portfolio_service.get_featured_articles(limit=articles_limit)
    }


@router.get("/portfolio-summary")
async def get_portfolio_summary():
    """Get a summary of portfolio statistics."""
    portfolio = portfolio_service.get_portfolio_data()
    
    return {
        "total_projects": len(portfolio.projects),
        "featured_projects": len([p for p in portfolio.projects if p.featured]),
        "total_articles": len(portfolio.articles),
        "featured_articles": len([a for a in portfolio.articles if a.featured]),
        "total_certifications": len(portfolio.certifications),
        "total_technologies": len(portfolio.tech_stack),
        "education_levels": len(portfolio.education)
    }
