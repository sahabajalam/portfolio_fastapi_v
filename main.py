"""
Modular FastAPI Portfolio Application
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routes import pages, api


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    
    # Initialize FastAPI app
    app = FastAPI(
        title=settings.app_name,
        description=settings.app_description,
        version=settings.version,
        debug=settings.debug
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=settings.allowed_methods,
        allow_headers=settings.allowed_headers,
    )
    
    # Mount static files
    app.mount("/static", StaticFiles(directory=settings.static_dir), name="static")
    app.mount("/assets", StaticFiles(directory=settings.assets_dir), name="assets")
    
    # Include routers
    app.include_router(pages.router, tags=["pages"])
    app.include_router(api.router, tags=["api"])
    
    return app


# Create the app instance
app = create_app()


if __name__ == "__main__":
    import uvicorn
    
    print(f"🚀 Starting {settings.app_name} FastAPI Server...")
    print(f"📱 Visit: http://{settings.host}:{settings.port}")
    print(f"📖 API Docs: http://{settings.host}:{settings.port}/docs")
    
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload
    )
