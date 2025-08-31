# PowerShell script to activate UV virtual environment and run the FastAPI application
.\.venv\Scripts\activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
