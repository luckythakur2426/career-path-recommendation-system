from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "Raw dataset.xlsx"

def load_data(filepath=DATA_PATH):
    """Validates file existence and loads raw Excel dataset."""
    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(f"Dataset file not found at: {filepath}")

    return pd.read_excel(filepath)

def clean_skill_string(skill_str):
    """Converts comma-separated skill string into a cleaned list."""
    if not skill_str:
        return []
    return [s.strip() for s in skill_str.split(",") if s.strip()]