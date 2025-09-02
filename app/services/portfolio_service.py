"""
Optimized Portfolio Service with improved data management and caching.
"""
from typing import List, Optional, Dict, Any
from datetime import datetime
from functools import lru_cache
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
            title="Junior Data Engineer & ML Engineer",
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
            ("Python", "fab fa-python", "Programming", 5),
            ("SQL", "fas fa-database", "Database", 4),
            ("Docker", "fab fa-docker", "DevOps", 4),
            ("AWS", "fab fa-aws", "Cloud", 4),
            ("PyTorch", "fas fa-brain", "ML Framework", 4),
            ("TensorFlow", "fas fa-robot", "ML Framework", 4),
            ("Kubernetes", "fas fa-dharmachakra", "DevOps", 3),
            ("PostgreSQL", "fas fa-server", "Database", 4),
            ("MongoDB", "fas fa-leaf", "Database", 3),
            ("FastAPI", "fas fa-rocket", "Framework", 4),
            ("Git", "fab fa-git-alt", "Tools", 5),
            ("MLOps", "fas fa-cogs", "Operations", 3),
            ("LangGraph", "fas fa-share-alt", "AI", 4),
            ("AutoGen", "fas fa-users", "AI", 4),
            ("LangChain", "fas fa-link", "AI", 4),
            ("Apache Airflow", "fas fa-project-diagram", "Data Pipeline", 4),
            ("Power BI", "fas fa-chart-bar", "BI", 3),
            ("React", "fab fa-react", "Frontend", 4),
            ("Streamlit", "fas fa-stream", "Frontend", 3),
            ("Redis", "fas fa-memory", "Database", 3),
            ("Scikit-learn", "fas fa-calculator", "ML Framework", 4),
            ("Grafana", "fas fa-chart-line", "Monitoring", 3),
            ("Pandas", "fas fa-table", "Data Science", 5),
            ("Computer Vision", "fas fa-eye", "AI", 4),
            ("NLP", "fas fa-language", "AI", 4),
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
        """Create articles data with factory method."""
        articles_data = [
            # Featured Articles
            {
                "id": "fine-tuning-llms",
                "title": "Fine-tuning LLMs on Custom Data: Complete Guide",
                "category": "Tutorial",
                "tags": ["LLM", "Fine-tuning", "AI", "Machine Learning"],
                "featured": True,
                "read_time": 8,
                "date": datetime(2024, 12, 10)
            },
            {
                "id": "mlops-best-practices",
                "title": "MLOps Best Practices for Production Systems",
                "category": "Best Practices",
                "tags": ["MLOps", "Production", "DevOps", "Machine Learning"],
                "featured": True,
                "read_time": 10,
                "date": datetime(2024, 11, 28)
            },
            
            # Tutorial Category
            {
                "id": "pytorch-fundamentals",
                "title": "PyTorch Fundamentals: Building Neural Networks",
                "category": "Tutorial",
                "tags": ["PyTorch", "Deep Learning", "Neural Networks"],
                "featured": False,
                "read_time": 12,
                "date": datetime(2024, 12, 8)
            },
            {
                "id": "data-preprocessing",
                "title": "Data Preprocessing Techniques for ML",
                "category": "Tutorial",
                "tags": ["Data Science", "Preprocessing", "Feature Engineering"],
                "featured": False,
                "read_time": 9,
                "date": datetime(2024, 12, 3)
            },
            {
                "id": "docker-ml-guide",
                "title": "Containerizing ML Models with Docker",
                "category": "Tutorial",
                "tags": ["Docker", "MLOps", "Deployment"],
                "featured": False,
                "read_time": 11,
                "date": datetime(2024, 11, 25)
            },
            {
                "id": "fastapi-ml-api",
                "title": "Building ML APIs with FastAPI",
                "category": "Tutorial",
                "tags": ["FastAPI", "API", "Machine Learning"],
                "featured": False,
                "read_time": 13,
                "date": datetime(2024, 11, 20)
            },
            {
                "id": "apache-kafka-streaming",
                "title": "Real-time Data Streaming with Apache Kafka",
                "category": "Tutorial",
                "tags": ["Kafka", "Streaming", "Data Engineering"],
                "featured": False,
                "read_time": 15,
                "date": datetime(2024, 11, 15)
            },
            
            # Analysis Category
            {
                "id": "ai-ethics",
                "title": "AI Ethics in Practice: Real-World Considerations",
                "category": "Analysis",
                "tags": ["AI Ethics", "Responsible AI", "Industry", "Governance"],
                "featured": False,
                "read_time": 6,
                "date": datetime(2024, 12, 5)
            },
            {
                "id": "transformer-architecture",
                "title": "Understanding Transformer Architecture",
                "category": "Analysis",
                "tags": ["Transformers", "NLP", "Architecture"],
                "featured": False,
                "read_time": 14,
                "date": datetime(2024, 11, 30)
            },
            {
                "id": "gpt-vs-bert",
                "title": "GPT vs BERT: A Comprehensive Comparison",
                "category": "Analysis",
                "tags": ["GPT", "BERT", "NLP", "Language Models"],
                "featured": False,
                "read_time": 10,
                "date": datetime(2024, 11, 22)
            },
            {
                "id": "ai-market-trends",
                "title": "AI Market Trends and Future Predictions",
                "category": "Analysis",
                "tags": ["AI Trends", "Market Analysis", "Industry"],
                "featured": False,
                "read_time": 8,
                "date": datetime(2024, 11, 10)
            },
            {
                "id": "data-privacy-ml",
                "title": "Data Privacy Challenges in Machine Learning",
                "category": "Analysis",
                "tags": ["Privacy", "GDPR", "Data Security"],
                "featured": False,
                "read_time": 7,
                "date": datetime(2024, 11, 5)
            },
            
            # Best Practices Category
            {
                "id": "model-versioning",
                "title": "Model Versioning and Experiment Tracking",
                "category": "Best Practices",
                "tags": ["MLflow", "Versioning", "Experiments"],
                "featured": False,
                "read_time": 9,
                "date": datetime(2024, 12, 1)
            },
            {
                "id": "code-quality-ml",
                "title": "Code Quality Best Practices in ML Projects",
                "category": "Best Practices",
                "tags": ["Code Quality", "Testing", "ML Engineering"],
                "featured": False,
                "read_time": 11,
                "date": datetime(2024, 11, 18)
            },
            {
                "id": "scalable-ml-systems",
                "title": "Building Scalable Machine Learning Systems",
                "category": "Best Practices",
                "tags": ["Scalability", "Architecture", "Systems Design"],
                "featured": False,
                "read_time": 13,
                "date": datetime(2024, 11, 12)
            },
            {
                "id": "feature-store-design",
                "title": "Feature Store Design Patterns",
                "category": "Best Practices",
                "tags": ["Feature Store", "ML Infrastructure", "Data Management"],
                "featured": False,
                "read_time": 12,
                "date": datetime(2024, 10, 28)
            },
            {
                "id": "monitoring-ml-models",
                "title": "Monitoring ML Models in Production",
                "category": "Best Practices",
                "tags": ["Monitoring", "Production", "Model Drift"],
                "featured": False,
                "read_time": 10,
                "date": datetime(2024, 10, 20)
            },
            
            # Technical Deep Dive Category
            {
                "id": "attention-mechanisms",
                "title": "Deep Dive into Attention Mechanisms",
                "category": "Technical Deep Dive",
                "tags": ["Attention", "Deep Learning", "Neural Networks"],
                "featured": False,
                "read_time": 16,
                "date": datetime(2024, 11, 8)
            },
            {
                "id": "gradient-descent-optimization",
                "title": "Gradient Descent Optimization Algorithms",
                "category": "Technical Deep Dive",
                "tags": ["Optimization", "Algorithms", "Mathematics"],
                "featured": False,
                "read_time": 14,
                "date": datetime(2024, 10, 25)
            },
            {
                "id": "distributed-training",
                "title": "Distributed Training Strategies for Deep Learning",
                "category": "Technical Deep Dive",
                "tags": ["Distributed Computing", "Deep Learning", "Scaling"],
                "featured": False,
                "read_time": 18,
                "date": datetime(2024, 10, 15)
            },
            {
                "id": "reinforcement-learning-fundamentals",
                "title": "Reinforcement Learning: From Theory to Practice",
                "category": "Technical Deep Dive",
                "tags": ["Reinforcement Learning", "Algorithms", "AI"],
                "featured": False,
                "read_time": 20,
                "date": datetime(2024, 10, 8)
            },
            {
                "id": "neural-architecture-search",
                "title": "Neural Architecture Search: Automated Design",
                "category": "Technical Deep Dive",
                "tags": ["NAS", "AutoML", "Neural Networks"],
                "featured": False,
                "read_time": 17,
                "date": datetime(2024, 9, 30)
            },
            
            # Research Category
            {
                "id": "multimodal-ai-research",
                "title": "Recent Advances in Multimodal AI Research",
                "category": "Research",
                "tags": ["Multimodal", "Research", "Computer Vision", "NLP"],
                "featured": False,
                "read_time": 12,
                "date": datetime(2024, 10, 12)
            },
            {
                "id": "quantum-ml-applications",
                "title": "Quantum Machine Learning Applications",
                "category": "Research",
                "tags": ["Quantum Computing", "Machine Learning", "Research"],
                "featured": False,
                "read_time": 15,
                "date": datetime(2024, 9, 28)
            },
            {
                "id": "federated-learning-privacy",
                "title": "Federated Learning and Privacy Preservation",
                "category": "Research",
                "tags": ["Federated Learning", "Privacy", "Distributed AI"],
                "featured": False,
                "read_time": 13,
                "date": datetime(2024, 9, 20)
            },
            {
                "id": "generative-ai-creativity",
                "title": "Generative AI and Creative Applications",
                "category": "Research",
                "tags": ["Generative AI", "Creativity", "Art", "Innovation"],
                "featured": False,
                "read_time": 11,
                "date": datetime(2024, 9, 15)
            }
        ]
        
        return [
            Article(
                id=a["id"],
                title=a["title"],
                excerpt=f"An insightful article about {a['title'].lower()} covering key concepts and practical implementations.",
                content=f"A comprehensive exploration of {a['title'].lower()} with detailed analysis and practical examples.",
                category=a["category"],
                tags=a["tags"],
                published_date=a["date"],
                read_time=a["read_time"],
                featured=a["featured"],
                image_url=None,
                external_url=f"https://medium.com/@sahabaj/{a['id']}"
            )
            for a in articles_data
        ]
    
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
