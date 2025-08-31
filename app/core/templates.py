"""
Template utilities and Jinja2 configuration.
"""
from pathlib import Path
from fastapi.templating import Jinja2Templates
from app.core.config import settings


class TemplateManager:
    """Manages Jinja2 templates with custom filters and globals."""
    
    def __init__(self):
        self.templates = Jinja2Templates(directory=settings.template_dir)
        self._setup_globals()
        self._setup_filters()
    
    def _setup_globals(self):
        """Add global variables available to all templates."""
        self.templates.env.globals.update({
            'app_name': settings.app_name,
            'contact_email': settings.contact_email,
            'linkedin_url': settings.linkedin_url,
            'github_url': settings.github_url,
            'twitter_url': settings.twitter_url,
            'medium_url': settings.medium_url,
        })
    
    def _setup_filters(self):
        """Add custom Jinja2 filters."""
        
        def format_date(date_string: str, format_type: str = "long") -> str:
            """Format date strings for display."""
            if format_type == "short":
                return date_string  # Could add actual date parsing here
            return date_string
        
        def truncate_text(text: str, length: int = 100) -> str:
            """Truncate text to specified length."""
            if len(text) <= length:
                return text
            return text[:length].strip() + "..."
        
        self.templates.env.filters.update({
            'format_date': format_date,
            'truncate': truncate_text,
        })
    
    def render(self, template_name: str, context: dict):
        """Render a template with the given context."""
        return self.templates.TemplateResponse(template_name, context)


# Global template manager instance
template_manager = TemplateManager()
