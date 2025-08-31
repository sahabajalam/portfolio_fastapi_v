"""
Portfolio data service - manages portfolio data and provides business logic.
"""
from typing import List, Optional
from datetime import datetime
from app.models.portfolio import (
    PortfolioData, PersonalInfo, ContactInfo, Education, 
    Certification, TechStack, Project, Article
)
from app.core.config import settings


class PortfolioService:
    """Service class for managing portfolio data."""
    
    def __init__(self):
        self._load_portfolio_data()
    
    def _load_portfolio_data(self):
        """Load portfolio data. In a real app, this might come from a database."""
        
        # Personal Information
        self.personal_info = PersonalInfo(
            name="Sahabaj Alam",
            title="Junior Data Scientist & ML Engineer",
            intro="Hi am Sahabaj Alam",
            bio="Passionate about leveraging data science and machine learning to drive innovation and improve decision-making.",
            location="UK",
            profile_image="assets/claude-color.svg"
        )
        
        # Contact Information
        self.contact_info = ContactInfo(
            email=settings.contact_email,
            linkedin=settings.linkedin_url,
            github=settings.github_url,
            twitter=settings.twitter_url,
            medium=settings.medium_url
        )
        
        # Education
        self.education = [
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
        
        # Certifications
        self.certifications = [
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
        
        # Tech Stack
        self.tech_stack = [
            TechStack(name="Python", icon="fab fa-python", category="Programming", proficiency=5),
            TechStack(name="SQL", icon="fas fa-database", category="Database", proficiency=4),
            TechStack(name="Docker", icon="fab fa-docker", category="DevOps", proficiency=4),
            TechStack(name="AWS", icon="fab fa-aws", category="Cloud", proficiency=4),
            TechStack(name="PyTorch", icon="fas fa-brain", category="ML Framework", proficiency=4),
            TechStack(name="TensorFlow", icon="fas fa-robot", category="ML Framework", proficiency=4),
            TechStack(name="Kubernetes", icon="fas fa-dharmachakra", category="DevOps", proficiency=3),
            TechStack(name="PostgreSQL", icon="fas fa-server", category="Database", proficiency=4),
            TechStack(name="MongoDB", icon="fas fa-leaf", category="Database", proficiency=3),
            TechStack(name="FastAPI", icon="fas fa-rocket", category="Framework", proficiency=4),
            TechStack(name="Git", icon="fab fa-git-alt", category="Tools", proficiency=5),
            TechStack(name="MLOps", icon="fas fa-cogs", category="Operations", proficiency=3),
            TechStack(name="LangGraph", icon="fas fa-share-alt", category="AI", proficiency=3),
            TechStack(name="Apache Airflow", icon="fas fa-project-diagram", category="Data Pipeline", proficiency=3),
            TechStack(name="PySpark", icon="fas fa-bolt", category="Big Data", proficiency=3),
            TechStack(name="VectorDB", icon="fas fa-vector-square", category="Database", proficiency=3),
        ]
        
        # Projects
        self.projects = [
            Project(
                id="ai-document-analysis",
                title="AI-Powered Document Analysis System",
                description="Advanced multi-modal AI system for intelligent document processing, extraction, and analysis using transformers and OCR technology. Built with state-of-the-art models for text extraction, document classification, and semantic understanding.",
                long_description="This comprehensive AI system combines computer vision, natural language processing, and deep learning to automatically process and analyze various document types. Features include intelligent text extraction from scanned documents, automatic document classification, semantic content analysis, and structured data extraction. The system uses transformer models for document understanding and OCR technology for text recognition.",
                tech_stack=["Transformers", "OCR", "FastAPI", "React", "PostgreSQL", "Docker"],
                category="ai",
                featured=True,
                github_url="https://github.com/sahabaj/ai-document-analysis",
                demo_url="https://doc-analysis-demo.com",
                image_url=None,  # No image available
                created_date=datetime(2024, 10, 15)
            ),
            Project(
                id="mlops-pipeline",
                title="MLOps Production Pipeline",
                description="End-to-end MLOps pipeline with automated training, testing, and deployment using Apache Airflow, MLflow, and Kubernetes. Includes model versioning, A/B testing, and monitoring dashboards.",
                long_description="A complete MLOps solution that automates the entire machine learning lifecycle from data ingestion to model deployment. Features automated model training with hyperparameter tuning, comprehensive testing suites, A/B testing framework, model versioning with MLflow, and real-time monitoring dashboards. Deployed on Kubernetes for scalability and reliability.",
                tech_stack=["Apache Airflow", "MLflow", "Kubernetes", "PyTorch", "AWS", "Grafana"],
                category="mlops",
                featured=True,
                github_url="https://github.com/sahabaj/mlops-pipeline",
                demo_url="https://mlops-dashboard-demo.com",
                image_url=None,  # No image available
                created_date=datetime(2024, 9, 20)
            ),
            Project(
                id="object-detection",
                title="Real-time Object Detection System",
                description="High-performance object detection system using YOLO v8 and OpenCV for real-time video analysis. Optimized for edge deployment with 60+ FPS processing capability.",
                long_description="State-of-the-art object detection system capable of processing video streams in real-time with exceptional accuracy. Uses YOLO v8 architecture optimized for speed and accuracy, supports multiple object classes, includes confidence scoring, and features web-based interface for live monitoring. Optimized for both cloud and edge deployment scenarios.",
                tech_stack=["YOLO", "OpenCV", "PyTorch", "FastAPI", "WebRTC"],
                category="computer-vision",
                featured=True,
                github_url="https://github.com/sahabaj/object-detection",
                demo_url="https://object-detect-demo.com",
                image_url=None,  # No image available
                created_date=datetime(2024, 8, 10)
            ),
            Project(
                id="stock-analyzer",
                title="Stock Price Analyzer & Predictor",
                description="Real-time stock analysis platform with LSTM-based price prediction, sentiment analysis from news, and interactive dashboards. Features risk assessment and portfolio optimization.",
                long_description="Comprehensive financial analysis platform that combines technical analysis, machine learning predictions, and sentiment analysis to provide actionable investment insights. Features include real-time price prediction using LSTM networks, news sentiment analysis, portfolio optimization algorithms, and interactive dashboards with customizable metrics and alerts.",
                tech_stack=["Flask", "LSTM", "Chart.js", "Alpha Vantage API", "Redis"],
                category="web-app",
                github_url="https://github.com/sahabaj/stock-analyzer",
                demo_url="https://stock-analyzer-demo.com",
                image_url=None,  # No image available
                created_date=datetime(2024, 7, 5)
            ),
            Project(
                id="chatbot-rag",
                title="RAG-based Intelligent Chatbot",
                description="Context-aware chatbot using Retrieval-Augmented Generation with vector databases. Supports multiple document formats and maintains conversation context.",
                long_description="Advanced conversational AI system that leverages Retrieval-Augmented Generation to provide accurate, contextual responses based on custom knowledge bases. Features document ingestion from multiple formats, vector-based similarity search, conversation memory, and fine-tuned response generation. Built with LangChain framework for robust AI orchestration.",
                tech_stack=["LangChain", "ChromaDB", "FastAPI", "Streamlit", "OpenAI"],
                category="ai",
                github_url="https://github.com/sahabaj/rag-chatbot",
                demo_url="https://rag-chatbot-demo.com",
                image_url=None,  # No image available
                created_date=datetime(2024, 6, 12)
            ),
            Project(
                id="data-pipeline",
                title="Real-time Data Processing Pipeline",
                description="Scalable data pipeline processing millions of events per day using Apache Kafka, Spark, and Delta Lake. Includes real-time analytics and anomaly detection.",
                long_description="Enterprise-grade data processing infrastructure capable of handling high-volume, real-time data streams. Features fault-tolerant architecture with Apache Kafka for event streaming, Apache Spark for distributed processing, Delta Lake for reliable data storage, and real-time anomaly detection using statistical and ML-based methods.",
                tech_stack=["Apache Kafka", "PySpark", "Delta Lake", "Kubernetes", "Grafana"],
                category="data-engineering",
                github_url="https://github.com/sahabaj/data-pipeline",
                demo_url="https://data-pipeline-dashboard.com",
                image_url=None,  # No image available
                created_date=datetime(2024, 5, 18)
            )
        ]
        
        # Articles
        self.articles = [
            Article(
                id="fine-tuning-llms",
                title="Fine-tuning LLMs on Custom Data: Complete Guide",
                excerpt="Learn how to adapt large language models for domain-specific tasks with practical examples and code implementations.",
                content="A comprehensive guide covering the entire process of fine-tuning large language models for specific use cases. This article walks through data preparation, model selection, training strategies, evaluation metrics, and deployment considerations with real-world examples.",
                category="Tutorial",
                tags=["LLM", "Fine-tuning", "AI", "Machine Learning"],
                published_date=datetime(2024, 12, 10),
                read_time=8,
                featured=True,
                image_url=None,  # No image available
                external_url="https://medium.com/@sahabaj/fine-tuning-llms-guide"
            ),
            Article(
                id="ai-ethics",
                title="AI Ethics in Practice: Real-World Considerations",
                excerpt="Exploring responsible AI development and deployment with case studies from leading tech companies.",
                content="An in-depth analysis of AI ethics in practice, covering bias detection and mitigation, fairness in ML systems, transparency requirements, and governance frameworks. Includes case studies from major tech companies and practical implementation strategies.",
                category="Analysis",
                tags=["AI Ethics", "Responsible AI", "Industry", "Governance"],
                published_date=datetime(2024, 12, 5),
                read_time=6,
                featured=False,
                image_url=None,  # No image available
                external_url="https://medium.com/@sahabaj/ai-ethics-practice"
            ),
            Article(
                id="mlops-best-practices",
                title="MLOps Best Practices for Production Systems",
                excerpt="Essential practices for deploying and maintaining machine learning models in production environments.",
                content="A practical guide to implementing MLOps in enterprise environments, covering CI/CD for ML, model monitoring, versioning strategies, automated testing, and infrastructure management. Includes real-world examples and tooling recommendations.",
                category="Best Practices",
                tags=["MLOps", "Production", "DevOps", "Machine Learning"],
                published_date=datetime(2024, 11, 28),
                read_time=10,
                featured=True,
                image_url=None,  # No image available
                external_url="https://medium.com/@sahabaj/mlops-best-practices"
            ),
            Article(
                id="vector-databases-guide",
                title="Vector Databases: The Foundation of Modern AI",
                excerpt="Understanding vector databases and their crucial role in AI applications like RAG, recommendation systems, and semantic search.",
                content="A comprehensive exploration of vector databases, covering their architecture, use cases, and implementation strategies. Discusses popular vector database solutions, performance considerations, and integration patterns with AI applications.",
                category="Technical Deep Dive",
                tags=["Vector Databases", "AI", "RAG", "Semantic Search"],
                published_date=datetime(2024, 11, 15),
                read_time=7,
                featured=False,
                image_url=None,  # No image available
                external_url="https://medium.com/@sahabaj/vector-databases-guide"
            )
        ]
    
    def get_portfolio_data(self) -> PortfolioData:
        """Get complete portfolio data."""
        return PortfolioData(
            personal_info=self.personal_info,
            contact_info=self.contact_info,
            education=self.education,
            certifications=self.certifications,
            tech_stack=self.tech_stack,
            projects=self.projects,
            articles=self.articles
        )
    
    def get_featured_projects(self, limit: int = 3) -> List[Project]:
        """Get featured projects."""
        featured = [p for p in self.projects if p.featured]
        return featured[:limit] if featured else self.projects[:limit]
    
    def get_featured_articles(self, limit: int = 2) -> List[Article]:
        """Get featured articles."""
        featured = [a for a in self.articles if a.featured]
        return featured[:limit] if featured else self.articles[:limit]
    
    def get_project_by_id(self, project_id: str) -> Optional[Project]:
        """Get a specific project by ID."""
        return next((p for p in self.projects if p.id == project_id), None)
    
    def get_article_by_id(self, article_id: str) -> Optional[Article]:
        """Get a specific article by ID."""
        return next((a for a in self.articles if a.id == article_id), None)
    
    def get_projects_by_category(self, category: str) -> List[Project]:
        """Get projects filtered by category."""
        return [p for p in self.projects if p.category.lower() == category.lower()]
    
    def get_tech_by_category(self, category: str) -> List[TechStack]:
        """Get technologies filtered by category."""
        return [t for t in self.tech_stack if t.category.lower() == category.lower()]


# Global portfolio service instance
portfolio_service = PortfolioService()
