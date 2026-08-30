import sys
from pathlib import Path

# Add backend directory to Python sys path
backend_path = Path(__file__).resolve().parent.parent / "backend"
sys.path.append(str(backend_path))

# Import your FastAPI app instance
from app.main import app