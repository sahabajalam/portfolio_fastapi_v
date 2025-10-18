"""
Optimized Portfolio Service with improved data management and caching.
"""
from typing import List, Optional, Dict, Any
from datetime import datetime
from functools import lru_cache
from collections import Counter
import json
from pathlib import Path
from app.models.portfolio import (
    PortfolioData, PersonalInfo, ContactInfo, Education, 
    Certification, TechStack, Project, Article
)
from app.core.config import settings


class OptimizedPortfolioService:
    """Optimized service class for managing portfolio data with caching."""
    
    def __init__(self):
        self._portfolio_data = None
        self._load_portfolio_data()
    
    @property
    def portfolio_data(self) -> PortfolioData:
        """Cached access to portfolio data."""
        if self._portfolio_data is None:
            self._load_portfolio_data()
        assert self._portfolio_data is not None
        return self._portfolio_data
    
    @property
    def personal_info(self) -> PersonalInfo:
        return self.portfolio_data.personal_info
    
    @property
    def contact_info(self) -> ContactInfo:
        return self.portfolio_data.contact_info
    
    @property
    def education(self) -> List[Education]:
        return self.portfolio_data.education
    
    @property
    def certifications(self) -> List[Certification]:
        return self.portfolio_data.certifications
    
    @property
    def tech_stack(self) -> List[TechStack]:
        return self.portfolio_data.tech_stack
    
    @property
    def projects(self) -> List[Project]:
        return self.portfolio_data.projects
    
    @property
    def articles(self) -> List[Article]:
        return self.portfolio_data.articles
    
    def _load_portfolio_data(self):
        """Load portfolio data with optimized data structures."""
        
        # Use data factory methods for cleaner code
        personal_info = self._create_personal_info()
        contact_info = self._create_contact_info()
        education = self._create_education_data()
        certifications = self._create_certifications_data()
        tech_stack = self._create_tech_stack_data()
        projects = self._create_projects_data()
        articles = self._create_articles_data()
        
        self._portfolio_data = PortfolioData(
            personal_info=personal_info,
            contact_info=contact_info,
            education=education,
            certifications=certifications,
            tech_stack=tech_stack,
            projects=projects,
            articles=articles
        )
    
    def _create_personal_info(self) -> PersonalInfo:
        """Create personal information."""
        return PersonalInfo(
            name="Sahabaj Alam",
            title="Junior AIML Engineer",
            intro="Hi am Sahabaj Alam",
            bio="Passionate about leveraging data science and machine learning to drive innovation and improve decision-making.",
            location="UK",
            profile_image="assets/claude-color.svg"
        )
    
    def _create_contact_info(self) -> ContactInfo:
        """Create contact information from settings."""
        return ContactInfo(
            email=settings.contact_email,
            linkedin=settings.linkedin_url,
            github=settings.github_url,
            twitter=settings.twitter_url,
            medium=settings.medium_url
        )
    
    def _create_education_data(self) -> List[Education]:
        """Create education data."""
        return [
            Education(
                degree="MSc Data Science & AI",
                institution="Bournemouth University",
                year="2024 - 2025",
                description="Advanced studies in data science, machine learning, and artificial intelligence with focus on practical applications and research.",
                current=True
            ),
            Education(
                degree="PG Diploma Data Science & AI",
                institution="University of Hyderabad",
                year="2021 - 2022",
                description="Comprehensive program covering statistical analysis, machine learning algorithms, and data visualization techniques."
            ),
            Education(
                degree="B.Tech Electronics & Communication",
                institution="Aliah University",
                year="2014 - 2018",
                description="Bachelor's degree in Electronics and Communication Engineering with strong foundation in mathematics and technical problem-solving."
            )
        ]
    
    def _create_certifications_data(self) -> List[Certification]:
        """Create certifications data."""
        return [
            Certification(
                title="TensorFlow Developer Certificate",
                issuer="TensorFlow",
                year="2024",
                credential_url="https://www.credential.net/tensorflow-developer",
                description="Professional certification demonstrating expertise in TensorFlow framework for machine learning and deep learning applications."
            ),
            Certification(
                title="Deep Learning Specialization",
                issuer="Coursera (Andrew Ng)",
                year="2023",
                credential_url="https://www.coursera.org/specializations/deep-learning",
                description="Comprehensive specialization covering neural networks, deep learning, and practical implementation of AI systems."
            ),
            Certification(
                title="IBM Data Science Professional Certificate",
                issuer="IBM",
                year="2023",
                credential_url="https://www.coursera.org/professional-certificates/ibm-data-science",
                description="Professional certificate program covering data science methodology, tools, and hands-on experience with real-world projects."
            )
        ]
    
    def _create_tech_stack_data(self) -> List[TechStack]:
        """Create technology stack data."""
        tech_data = [
            ("Python", "devicon-python-plain colored", "Programming", 5),  # Official Python icon
            ("FastAPI", "devicon-fastapi-plain colored", "Framework", 4),  # Official FastAPI icon
            ("PyTorch", "devicon-pytorch-original colored", "ML Framework", 4),  # Official PyTorch icon
            ("LangChain", "fas fa-link", "AI", 4),  # No official icon - chain links
            ("LangGraph", "fas fa-project-diagram", "AI", 4),  # No official icon - graph/diagram
            ("AutoGen", "fas fa-robot", "AI", 4),  # No official icon - robot
            ("Neo4j", "devicon-neo4j-plain colored", "Database", 4),  # Official Neo4j icon
            ("GraphRAG", "fas fa-diagram-project", "AI", 4),  # No official icon - diagram
            ("FAISS", "fas fa-vector-square", "AI", 4),  # No official icon - vector
            ("Docker", "devicon-docker-plain colored", "DevOps", 4),  # Official Docker icon
            ("Kubernetes", "devicon-kubernetes-plain colored", "DevOps", 4),  # Official Kubernetes icon
            ("AWS", "devicon-amazonwebservices-plain colored", "Cloud", 4),  # Official AWS icon
            ("PostgreSQL", "devicon-postgresql-plain colored", "Database", 4),  # Official PostgreSQL icon
            ("MLOps", "fas fa-gears", "Operations", 4),  # Concept - gears
            ("Apache Airflow", "devicon-apacheairflow-plain colored", "Data Pipeline", 4),  # Official Airflow icon
            # Devicon doesn't provide MLflow yet; use Simple Icons SVG for official logo
            ("MLflow", "https://cdn.simpleicons.org/mlflow/0194E2", "MLOps", 4),
        ]
        
        return [
            TechStack(name=name, icon=icon, category=category, proficiency=proficiency)
            for name, icon, category, proficiency in tech_data
        ]
    
    def _create_projects_data(self) -> List[Project]:
        """Create projects data with factory method."""
        projects_data = [
            {
                "id": "automated-data-science-pipeline",
                "title": "Automated Data Science Pipeline with LangGraph",
                "description": "End-to-end automated data science pipeline leveraging LangGraph for orchestrating complex ML workflows, from data ingestion to model deployment.",
                "tech_stack": ["LangGraph", "Python", "Apache Airflow", "MLflow", "Docker", "Kubernetes", "Pandas"],
                "image_url": "assets/project_card/automated-data-science-pipeline.png",
                "category": "ai",
                "featured": True,
                "date": datetime(2024, 10, 15)
            },
            {
                "id": "healthcare-diagnosis-assistant",
                "title": "Intelligent Healthcare Diagnosis Assistant",
                "description": "AI-powered diagnostic assistant for healthcare professionals, combining medical imaging analysis, symptom checking, and treatment recommendations.",
                "tech_stack": ["PyTorch", "Computer Vision", "NLP", "FastAPI", "MongoDB", "Docker", "OpenCV"],
                "image_url": "assets/project_card/healthcare-diagnosis-assistant.png",
                "category": "healthcare",
                "featured": False,
                "date": datetime(2024, 5, 18)
            },
            {
                "id": "multi-agent-customer-analytics",
                "title": "Multi-Agent Customer Analytics Platform",
                "description": "Intelligent customer analytics platform using multiple AI agents for customer segmentation, behavior analysis, and personalized recommendations.",
                "tech_stack": ["AutoGen", "LangChain", "Python", "Redis", "MongoDB", "Streamlit", "Scikit-learn"],
                "image_url": "assets/project_card/multi-agent-customer-analytics.png",
                "category": "analytics",
                "featured": True,
                "date": datetime(2024, 8, 10)
            },
            {
                "id": "autonomous-ab-testing",
                "title": "Autonomous A/B Testing Framework",
                "description": "Self-optimizing A/B testing framework that automatically designs, executes, and analyzes experiments using statistical methods and machine learning.",
                "tech_stack": ["Python", "Scikit-learn", "CausalML", "PostgreSQL", "FastAPI", "Docker", "Grafana"],
                "image_url": "assets/project_card/autonomous-ab-testing.png",
                "category": "mlops",
                "featured": False,
                "date": datetime(2024, 7, 5)
            },
            {
                "id": "ai-financial-analysis",
                "title": "AI-Powered Financial Analysis System",
                "description": "Advanced financial analysis system using AI for market prediction, risk assessment, portfolio optimization, and automated trading signals.",
                "tech_stack": ["TensorFlow", "Pandas", "NumPy", "Python", "FastAPI", "Alpha Vantage API", "Scikit-learn"],
                "image_url": "assets/project_card/ai-financial-analysis.png",
                "category": "finance",
                "featured": False,
                "date": datetime(2024, 6, 12)
            },
            {
                "id": "enterprise-bi-autogen-dashboard",
                "title": "Enterprise BI + AutoGen Agent Dashboard",
                "description": "Comprehensive business intelligence dashboard powered by AutoGen agents for automated report generation, insights discovery, and interactive data visualization.",
                "tech_stack": ["AutoGen", "Power BI", "React", "FastAPI", "Python", "PostgreSQL", "DAX"],
                "image_url": "assets/project_card/enterprise-bi-autogen-dashboard.png",
                "category": "bi",
                "featured": True,
                "date": datetime(2024, 9, 20)
            }
        ]
        
        return [
            Project(
                id=p["id"],
                title=p["title"],
                description=p["description"],
                long_description=f"A comprehensive project focused on {p['description'].lower()}. This project demonstrates advanced technical skills and practical application of modern technologies.",
                tech_stack=p["tech_stack"],
                category=p["category"],
                featured=p["featured"],
                github_url=f"https://github.com/sahabaj/{p['id']}",
                demo_url=f"https://{p['id']}-demo.com",
                image_url=p.get("image_url"),
                created_date=p["date"]
            )
            for p in projects_data
        ]
    
    def _create_articles_data(self) -> List[Article]:
        """Load articles data from JSON file."""
        articles_file = Path(__file__).parent.parent.parent / "data" / "articles.json"
        
        try:
            with open(articles_file, 'r', encoding='utf-8') as f:
                articles_data = json.load(f)
            
            return [
                Article(
                    id=a["id"],
                    title=a["title"],
                    excerpt=a.get("excerpt", ""),
                    content=a.get("content"),
                    category=a["category"],
                    tags=a["tags"],
                    published_date=datetime.fromisoformat(a["published_date"]),
                    read_time=a["read_time"],
                    featured=a.get("featured", False),
                    image_url=a.get("image_url"),
                    external_url=a.get("external_url")
                )
                for a in articles_data
            ]
        except FileNotFoundError:
            print(f"Warning: Articles file not found at {articles_file}. Using empty list.")
            return []
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse articles JSON: {e}. Using empty list.")
            return []
        except Exception as e:
            print(f"Error loading articles: {e}. Using empty list.")
            return []
    
    # Optimized getter methods with better error handling
    def get_portfolio_data(self) -> PortfolioData:
        """Get complete portfolio data."""
        return self.portfolio_data
    
    @lru_cache(maxsize=10)
    def get_featured_projects(self, limit: int = 3) -> List[Project]:
        """Get featured projects with caching."""
        featured = [p for p in self.projects if p.featured]
        return featured[:limit] if featured else self.projects[:limit]
    
    @lru_cache(maxsize=10)
    def get_featured_articles(self, limit: int = 2) -> List[Article]:
        """Get featured articles with caching."""
        featured = [a for a in self.articles if a.featured]
        return featured[:limit] if featured else self.articles[:limit]
    
    def get_project_by_id(self, project_id: str) -> Optional[Project]:
        """Get a specific project by ID with optimized lookup."""
        return next((p for p in self.projects if p.id == project_id), None)
    
    def get_article_by_id(self, article_id: str) -> Optional[Article]:
        """Get a specific article by ID with optimized lookup."""
        return next((a for a in self.articles if a.id == article_id), None)
    
    @lru_cache(maxsize=20)
    def get_projects_by_category(self, category: str) -> List[Project]:
        """Get projects filtered by category with caching."""
        return [p for p in self.projects if p.category.lower() == category.lower()]
    
    @lru_cache(maxsize=20)
    def get_tech_by_category(self, category: str) -> List[TechStack]:
        """Get technologies filtered by category with caching."""
        return [t for t in self.tech_stack if t.category.lower() == category.lower()]
    
    @lru_cache(maxsize=20)
    def get_articles_by_category(self, category: str) -> List[Article]:
        """Get articles filtered by category with caching."""
        return [a for a in self.articles if a.category.lower() == category.lower()]
    
    def get_category_counts(self) -> Dict[str, int]:
        """Get count of articles per category."""
        from collections import Counter
        categories = [article.category for article in self.articles]
        counts = Counter(categories)
        # Ensure all expected categories are present with 0 if not
        expected_categories = [
            "Machine Learning", "Deep Learning", "NLP", "Computer Vision", 
            "AI Research", "MLOps", "Data Engineering", "Reinforcement Learning", 
            "Security & Privacy", "Data Visualization", "Tools & Libraries"
        ]
        for cat in expected_categories:
            if cat not in counts:
                counts[cat] = 0
        return dict(counts)
    
    def get_portfolio_stats(self) -> Dict[str, Any]:
        """Get portfolio statistics."""
        return {
            "total_projects": len(self.projects),
            "featured_projects": len([p for p in self.projects if p.featured]),
            "total_articles": len(self.articles),
            "featured_articles": len([a for a in self.articles if a.featured]),
            "total_certifications": len(self.certifications),
            "total_technologies": len(self.tech_stack),
            "education_levels": len(self.education)
        }


# Global optimized portfolio service instance
portfolio_service = OptimizedPortfolioService()
