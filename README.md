# 🚀 FastAPI Portfolio

A modern, modular FastAPI portfolio application with clean architecture and responsive design. Built with **UV package management** for faster development and optimized performance.

## 📁 Project Structure
```
📦 fastapiport_v1/
├── 📄 main.py                    # Application entry point
├── 📄 requirements.txt           # Python dependencies
├── 📄 requirements.lock          # Locked dependency versions
├── 📄 pyproject.toml            # Modern Python project configuration
├── 📄 run_dev.ps1               # Quick development script
├── 📁 app/                      # Main application package
│   ├── 📁 core/                 # Core configuration and utilities
│   │   ├── config.py            # Application settings
│   │   └── templates.py         # Template configuration
│   ├── 📁 models/               # Data models
│   │   └── portfolio.py         # Portfolio data models
│   ├── 📁 routes/               # API routes
│   │   ├── api.py               # API endpoints
│   │   └── pages.py             # Page routes
│   ├── 📁 services/             # Business logic
│   │   └── portfolio_service.py # Portfolio data service
│   └── 📁 templates/            # Jinja2 templates
│       ├── base.html            # Base template
│       ├── 📁 pages/            # Page templates
│       └── 📁 components/       # Reusable components
├── 📁 static/                   # Static assets
│   ├── 📁 css/
│   │   └── 📁 modules/          # Modular CSS architecture
│   └── 📁 js/
│       └── 📁 modules/          # Optimized JavaScript modules
└── 📁 assets/                   # Media files
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- UV package manager (faster than pip)

### Setup with UV (Recommended)
```powershell
# Install UV (if not already installed)
pip install uv

# Create virtual environment
uv venv

# Activate virtual environment
.\.venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt

# Start development server (using helper script)
.\run_dev.ps1
```

### Alternative Setup (Traditional pip)
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start server
python main.py
```

Visit: http://localhost:8000

## ⚡ UV Package Management Benefits

This project uses **UV** for faster package management:
- **5-10x faster** package installation
- **Better dependency resolution**
- **Drop-in replacement** for pip
- **Enhanced caching** and performance

### UV Commands
```powershell
# Package management
uv pip install package_name      # Install package
uv pip uninstall package_name    # Remove package
uv pip list                      # List packages
uv pip freeze > requirements.txt # Update requirements

# Lock dependencies for reproducible builds
uv pip compile requirements.txt --output-file requirements.lock
```

## 🌐 API Endpoints

### Page Routes
- **GET /** - Home page with hero section and chat interface
- **GET /projects** - Projects showcase page
- **GET /articles** - Articles and blog posts page

### API Routes
- **GET /api/health** - Application health check
- **GET /api/contact** - Contact information
- **GET /api/projects** - Projects data (JSON)
- **GET /api/articles** - Articles data (JSON)
- **GET /docs** - Interactive API documentation (Swagger UI)

## 🏗️ Architecture

### Modular Design
- **Separation of Concerns**: Clear separation between models, services, routes, and templates
- **Reusable Components**: Modular templates and JavaScript for maintainability
- **Configuration Management**: Centralized settings with environment variables
- **Clean Dependencies**: Minimal, focused dependencies

### JavaScript Modules
- **NavigationManager**: Handles navigation, mobile menu, and smooth scrolling
- **ChatManager**: Interactive chat interface with contextual responses
- **AnimationManager**: Scroll animations and UI effects

### Template System
- **Base Template**: Shared layout with navigation and footer
- **Component Templates**: Reusable UI components
- **Page Templates**: Specific page layouts

## 🚀 Deployment

### Environment Variables
Create a `.env` file or set environment variables:
```bash
APP_NAME=Portfolio
HOST=0.0.0.0
PORT=8000
DEBUG=False
CONTACT_EMAIL=your.email@example.com
```

### Railway (Recommended)
```bash
# Connect your GitHub repository to Railway
# Auto-deploy with zero configuration
```

### Heroku
```bash
# Create Procfile
echo "web: uvicorn main:app --host=0.0.0.0 --port=\$PORT" > Procfile

# Deploy
heroku create your-portfolio
git push heroku main
```

### Docker
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🔧 Customization

### Adding New Pages
1. Create template in `app/templates/pages/`
2. Add route in `app/routes/pages.py`
3. Update navigation in `app/templates/components/navigation.html`

### Adding API Endpoints
1. Add data models in `app/models/`
2. Implement business logic in `app/services/`
3. Create API routes in `app/routes/api.py`

### Extending JavaScript
1. Create new module in `static/js/modules/`
2. Import in `app/templates/base.html`
3. Initialize in the main script section

## 🎨 Features

- ✅ **Responsive Design**: Mobile-first responsive layout
- ✅ **Interactive Chat**: AI-powered chat interface
- ✅ **Smooth Animations**: CSS and JavaScript animations
- ✅ **SEO Optimized**: Proper meta tags and structure
- ✅ **Fast Loading**: Optimized assets and lazy loading
- ✅ **Modern Stack**: FastAPI, Jinja2, ES6 modules
- ✅ **Clean Code**: Modular, maintainable architecture

## 📈 Performance

- **Fast Startup**: < 1s application startup time
- **Efficient Routing**: FastAPI's high-performance routing
- **Optimized Assets**: Compressed CSS and modular JavaScript
- **Responsive Images**: Proper image optimization and fallbacks

## 🛠️ Development

### Adding New Features
1. Plan the feature architecture
2. Create/update models if needed
3. Implement business logic in services
4. Add routes and templates
5. Update JavaScript modules if needed
6. Test and document

### Code Style
- Follow PEP 8 for Python code
- Use clear, descriptive variable names
- Comment complex logic
- Keep functions focused and small

## 📚 Documentation

- **API Docs**: Available at `/docs` endpoint
- **Code Comments**: Inline documentation
- **Type Hints**: Full type annotation coverage
- **README**: This comprehensive guide

Your portfolio is now a modern, scalable FastAPI application! 🎉
