# UV Package Management Setup

This project now uses UV for package management instead of pip.

## Setup Instructions

1. **Install UV** (if not already installed):
   ```powershell
   pip install uv
   ```

2. **Create Virtual Environment**:
   ```powershell
   uv venv
   ```

3. **Activate Virtual Environment**:
   ```powershell
   .\.venv\Scripts\activate
   ```

4. **Install Dependencies**:
   ```powershell
   uv pip install -r requirements.txt
   ```

## Running the Application

### Option 1: Manual
```powershell
.\.venv\Scripts\activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Option 2: Using the dev script
```powershell
.\run_dev.ps1
```

## Package Management with UV

- **Install a new package**: `uv pip install package_name`
- **Uninstall a package**: `uv pip uninstall package_name`
- **List installed packages**: `uv pip list`
- **Update requirements.txt**: `uv pip freeze > requirements.txt`

## Benefits of UV

- Faster package installation and resolution
- Better dependency management
- More efficient virtual environment handling
- Drop-in replacement for pip with enhanced performance
