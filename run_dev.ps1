# PowerShell script to activate UV virtual environment and run the FastAPI application
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
