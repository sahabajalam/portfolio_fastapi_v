"""
Core configuration for the Portfolio FastAPI application.
"""
from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    # App Configuration
    app_name: str = Field(default="Sahabaj Alam", description="Application name")
    app_description: str = Field(default="Personal Portfolio Website", description="Application description")
    version: str = Field(default="1.0.0", description="Application version")
    debug: bool = Field(default=False, description="Debug mode")
    
    # Server Configuration
    host: str = Field(default="0.0.0.0", description="Server host")
    port: int = Field(default=8000, description="Server port")
    reload: bool = Field(default=False, description="Auto-reload on changes")
    
    # Template Configuration
    template_dir: str = Field(default="app/templates", description="Templates directory")
    static_dir: str = Field(default="static", description="Static files directory")
    assets_dir: str = Field(default="assets", description="Assets directory")
    data_dir: str = Field(default="data", description="Data directory")
    
    # CORS Configuration
    allowed_origins: List[str] = Field(default=["https://portfolio-fastapi-v.onrender.com", "http://localhost:3000", "http://localhost:8000"], description="Allowed CORS origins")
    allowed_methods: List[str] = Field(default=["GET", "POST", "PUT", "DELETE", "OPTIONS"], description="Allowed HTTP methods")
    allowed_headers: List[str] = Field(default=["*"], description="Allowed headers")
    
    # Contact Information
    contact_email: str = Field(default="aisahabaj@gmail.com", description="Contact email")
    linkedin_url: str = Field(default="https://linkedin.com/in/sahabajalam", description="LinkedIn profile")
    github_url: str = Field(default="https://github.com/sahabajalam", description="GitHub profile")
    twitter_url: str = Field(default="https://x.com/sahabaj_alam", description="Twitter profile")
    medium_url: str = Field(default="https://medium.com/@sahabaj1101", description="Medium profile")
    
    # Security Configuration
    secret_key: str = Field(default="your-super-secret-key-change-this-in-prod", description="Secret key for JWT")
    algorithm: str = Field(default="HS256", description="Algorithm for JWT")
    access_token_expire_minutes: int = Field(default=30, description="Token expiration time")
    
    # Admin Credentials (should be set via env vars in production)
    admin_username: str = Field(default="admin", description="Admin username")
    admin_password: str = Field(default="admin123", description="Admin password")
    admin_totp_secret: str = Field(default="JBSWY3DPEHPK3PXP", description="TOTP Secret (Base32)")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance
settings = Settings()
