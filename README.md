# 🚀 Sahabaj Alam - AI Portfolio

A modern, high-performance portfolio website built with **FastAPI**, **Jinja2**, and **Modular CSS/JS**. This project showcases my work as an AI/ML Engineer, featuring a dynamic project gallery and a dedicated "NoteonAI" section for technical articles.

## 🌟 Key Features

- **⚡ High Performance**: Built on FastAPI for lightning-fast response times.
- **📱 Fully Responsive**: Mobile-first design ensuring a great experience on all devices.
- **🧠 NoteonAI**: A dedicated, data-driven blog section for AI/ML insights (formerly Articles).
- **🎨 Modular Architecture**: Clean separation of concerns with modular CSS, JavaScript, and Jinja2 templates.
- **💬 Interactive Chat**: Integrated chat interface for user engagement.
- **🔍 SEO Optimized**: Server-side rendering with Jinja2 for better search engine visibility.

## 🛠️ Tech Stack

- **Backend**: Python 3.11+, FastAPI, Uvicorn
- **Templating**: Jinja2
- **Frontend**: HTML5, CSS3 (Modular), JavaScript (ES6 Modules), TailwindCSS (Utility classes)
- **Data Storage**: JSON-based flat files for easy content management (Projects & Notes)
- **Package Management**: UV (for blazing fast dependency resolution)

## 📁 Project Structure

```
portfolio_v2/
├── app/
│   ├── core/                 # Config & Settings
│   ├── models/               # Pydantic Models
│   ├── routes/               # URL Routing (Pages & API)
│   ├── services/             # Business Logic (Data loading, filtering)
│   └── templates/            # Jinja2 HTML Templates
│       ├── components/       # Reusable UI parts (Navbar, Footer, Cards)
│       └── pages/            # Main Page Layouts (Home, Projects, NoteonAI)
├── data/                     # JSON Content
│   └── noteonai.json         # Blog posts data
├── static/                   # Public Assets
│   ├── css/modules/          # Component-specific CSS
│   ├── js/modules/           # Interactive JS modules
│   └── assets/               # Images & Icons
├── main.py                   # App Entry Point
└── requirements.txt          # Dependencies
```

## 🚀 Getting Started

### Prerequisites
- Python 3.11 or higher
- Git

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/sahabajalam/portfolio_fastapi_v.git
    cd portfolio_fastapi_v
    ```

2.  **Set up Virtual Environment (using UV is recommended)**
    ```bash
    # Install uv if you haven't
    pip install uv

    # Create venv
    uv venv

    # Activate venv
    # Windows:
    .venv\Scripts\activate
    # Mac/Linux:
    source .venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    uv pip install -r requirements.txt
    ```

4.  **Run the Application**
    ```bash
    # Using the helper script (Windows)
    .\run_dev.ps1

    # OR manually
    uvicorn main:app --reload
    ```

5.  **Visit the Site**
    Open [http://localhost:8000](http://localhost:8000) in your browser.

## 🧭 Navigation & Routes

- **Home**: `/` - Landing page with About & Contact sections.
- **Projects**: `/projects` - Showcase of AI/ML projects.
- **NoteonAI**: `/noteonai` - Technical articles and notes (formerly `/articles`).
- **API Docs**: `/docs` - Swagger UI for the backend API.

## 📝 Content Management

Content is managed via JSON files in the `data/` directory, making it easy to add new projects or notes without touching the code.

- **Add a Note**: Edit `data/noteonai.json`.
- **Add a Project**: Currently managed in `app/services/portfolio_service.py` (can be moved to JSON).

## 🚢 Deployment

The application is production-ready and includes configuration for:
- **Render**: `render.yaml`, `render-build.sh`, `render-start.sh`
- **Docker**: `Dockerfile` available for containerized deployment.

---
*Built with ❤️ by Sahabaj Alam*
