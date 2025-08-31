"""
Data models for the portfolio application.
"""
from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime


class ContactInfo(BaseModel):
    """Contact information model."""
    email: str = Field(..., description="Email address")
    linkedin: str = Field(..., description="LinkedIn profile URL")
    github: str = Field(..., description="GitHub profile URL")
    twitter: Optional[str] = Field(None, description="Twitter profile URL")
    medium: Optional[str] = Field(None, description="Medium profile URL")


class TechStack(BaseModel):
    """Technology stack item."""
    name: str = Field(..., description="Technology name")
    icon: str = Field(..., description="Icon class or identifier")
    category: str = Field(..., description="Technology category")
    proficiency: Optional[int] = Field(None, ge=1, le=5, description="Proficiency level (1-5)")


class Project(BaseModel):
    """Project model."""
    id: str = Field(..., description="Unique project identifier")
    title: str = Field(..., description="Project title")
    description: str = Field(..., description="Project description")
    long_description: Optional[str] = Field(None, description="Detailed project description")
    image_url: Optional[str] = Field(None, description="Project image URL")
    tech_stack: List[str] = Field(default_factory=list, description="Technologies used")
    demo_url: Optional[str] = Field(None, description="Live demo URL")
    github_url: Optional[str] = Field(None, description="GitHub repository URL")
    category: str = Field(..., description="Project category")
    featured: bool = Field(default=False, description="Whether project is featured")
    created_date: Optional[datetime] = Field(None, description="Project creation date")


class Article(BaseModel):
    """Article/blog post model."""
    id: str = Field(..., description="Unique article identifier")
    title: str = Field(..., description="Article title")
    excerpt: str = Field(..., description="Article excerpt")
    content: Optional[str] = Field(None, description="Full article content")
    image_url: Optional[str] = Field(None, description="Article image URL")
    category: str = Field(..., description="Article category")
    tags: List[str] = Field(default_factory=list, description="Article tags")
    published_date: datetime = Field(..., description="Publication date")
    read_time: int = Field(..., ge=1, description="Estimated read time in minutes")
    featured: bool = Field(default=False, description="Whether article is featured")
    external_url: Optional[str] = Field(None, description="External article URL")


class Education(BaseModel):
    """Education model."""
    degree: str = Field(..., description="Degree title")
    institution: str = Field(..., description="Educational institution")
    year: str = Field(..., description="Year or year range")
    description: Optional[str] = Field(None, description="Additional details")
    current: bool = Field(default=False, description="Whether currently enrolled")


class Certification(BaseModel):
    """Certification model."""
    title: str = Field(..., description="Certification title")
    issuer: str = Field(..., description="Issuing organization")
    year: str = Field(..., description="Year obtained")
    credential_url: Optional[str] = Field(None, description="Credential verification URL")
    description: Optional[str] = Field(None, description="Additional details")


class PersonalInfo(BaseModel):
    """Personal information model."""
    name: str = Field(..., description="Full name")
    title: str = Field(..., description="Professional title")
    intro: str = Field(..., description="Brief introduction")
    bio: str = Field(..., description="Detailed biography")
    location: Optional[str] = Field(None, description="Current location")
    profile_image: Optional[str] = Field(None, description="Profile image URL")


class PortfolioData(BaseModel):
    """Complete portfolio data model."""
    personal_info: PersonalInfo
    contact_info: ContactInfo
    education: List[Education]
    certifications: List[Certification]
    tech_stack: List[TechStack]
    projects: List[Project]
    articles: List[Article]
