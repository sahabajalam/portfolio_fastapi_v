# UV-enhanced development scripts for FastAPI Portfolio

## Development Commands

### Start Development Server
```powershell
# Using the helper script
.\run_dev.ps1

# Or manually
.\.venv\Scripts\activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Install Development Dependencies
```powershell
.\.venv\Scripts\activate
uv pip install pytest pytest-asyncio httpx black flake8 mypy
```

### Update Dependencies
```powershell
.\.venv\Scripts\activate
# Update a specific package
uv pip install --upgrade fastapi

# Regenerate lock file after updates
uv pip compile requirements.txt --output-file requirements.lock
```

### Code Quality Tools
```powershell
.\.venv\Scripts\activate

# Format code with Black
black .

# Lint with Flake8
flake8 app/ main.py

# Type checking with MyPy
mypy app/ main.py
```

### Testing
```powershell
.\.venv\Scripts\activate
pytest tests/
```

### Git Workflow with UV

Your existing Git repository works perfectly with UV! Here's the recommended workflow:

1. **Make changes to your code**
2. **Update dependencies if needed**:
   ```powershell
   .\.venv\Scripts\activate
   uv pip install new-package
   uv pip freeze > requirements.txt
   uv pip compile requirements.txt --output-file requirements.lock
   ```
3. **Commit changes**:
   ```powershell
   git add .
   git commit -m "Your commit message"
   git push origin main
   ```

### Files in Git

**Tracked files:**
- `requirements.txt` - Main dependencies
- `requirements.lock` - Locked versions (recommended to track)
- `pyproject.toml` - Project configuration
- All your source code

**Ignored files (already in .gitignore):**
- `.venv/` - Virtual environment
- `__pycache__/` - Python bytecode
- `uv.lock` - UV's internal lock file
