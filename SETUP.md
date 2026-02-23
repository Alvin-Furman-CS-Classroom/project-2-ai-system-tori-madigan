# Python Environment Setup Guide

## Quick Start

### 1. Create Virtual Environment

```powershell
# Windows PowerShell
py -m venv venv
```

### 2. Activate Virtual Environment

**Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

If you get an execution policy error:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Windows Command Prompt:**
```cmd
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Verify Setup

```powershell
python --version
pytest --version
```

## Running Tests

```powershell
# Run all tests
pytest unit_tests/

# Run specific test file
pytest unit_tests/test_module1_data_structures.py

# Run with verbose output
pytest -v unit_tests/
```

## Deactivating Virtual Environment

When you're done working:
```powershell
deactivate
```

## Troubleshooting

### Python not found
- Make sure Python is installed: `py --version`
- If `py` doesn't work, try `python` or `python3`

### Virtual environment activation fails
- Make sure you're in the project root directory
- Check that `venv` folder exists
- On Windows, you may need to change execution policy (see step 2 above)

### Import errors when running tests
- Make sure virtual environment is activated
- Make sure you're running from project root directory
- Check that `src/` directory is in Python path (tests handle this automatically)
