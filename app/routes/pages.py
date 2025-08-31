"""
Optimized page routes with consolidated context building.
"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from typing import Dict, Any, Optional
from app.core.templates import template_manager
from app.services.portfolio_service import portfolio_service

router = APIRouter()


class ContextBuilder:
    """Centralized context building service to eliminate duplication."""
    
    @staticmethod
    def build_base_context(
        request: Request, 
        page_title: str, 
        include_portfolio: bool = True
    ) -> Dict[str, Any]:
        """Build base context that's common to all pages."""
        context = {
            "request": request,
            "page_title": page_title
        }
        
        if include_portfolio:
            context["portfolio"] = portfolio_service.get_portfolio_data()
        
        return context
    
    @staticmethod
    def add_featured_content(
        context: Dict[str, Any], 
        projects_limit: int = 3, 
        articles_limit: int = 2
    ) -> Dict[str, Any]:
        """Add featured projects and articles to context."""
        context.update({
            "featured_projects": portfolio_service.get_featured_projects(limit=projects_limit),
            "featured_articles": portfolio_service.get_featured_articles(limit=articles_limit)
        })
        return context


@router.get("/", response_class=HTMLResponse)
@router.get("/index.html", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the home page with portfolio data."""
    context = ContextBuilder.build_base_context(request, "Sahabaj Alam")
    context = ContextBuilder.add_featured_content(context)
    
    return template_manager.render("pages/index.html", context)


@router.get("/projects", response_class=HTMLResponse)
@router.get("/projects.html", response_class=HTMLResponse)
async def projects(request: Request):
    """Serve the projects page."""
    context = ContextBuilder.build_base_context(request, "Projects")
    context["projects"] = context["portfolio"].projects
    
    return template_manager.render("pages/projects.html", context)


@router.get("/articles", response_class=HTMLResponse)
@router.get("/articles.html", response_class=HTMLResponse)
async def articles(request: Request):
    """Serve the articles page."""
    context = ContextBuilder.build_base_context(request, "Articles")
    context["articles"] = context["portfolio"].articles
    
    return template_manager.render("pages/articles.html", context)


@router.get("/all-articles", response_class=HTMLResponse)
@router.get("/all-articles.html", response_class=HTMLResponse)
async def all_articles(request: Request):
    """Serve the all articles page with filtering and pagination."""
    context = ContextBuilder.build_base_context(request, "All Articles")
    context["articles"] = context["portfolio"].articles
    
    return template_manager.render("pages/all_articles.html", context)


# Optional: Add a generic page renderer for future extensibility
@router.get("/{page_name}.html", response_class=HTMLResponse)
async def generic_page(request: Request, page_name: str):
    """Generic page renderer for simple pages."""
    try:
        # Attempt to render the page if template exists
        context = ContextBuilder.build_base_context(
            request, 
            page_name.replace("-", " ").replace("_", " ").title()
        )
        
        return template_manager.render(f"pages/{page_name}.html", context)
    except Exception:
        # Return 404 if template doesn't exist
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Page not found")
