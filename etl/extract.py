import pandas as pd
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def extract_data(file_path=None):
    """
    Extract data from a source (CSV in this example)
    """
    if file_path is None:
        # Get the absolute path to the input file
        base_dir = Path(__file__).parent.parent
        default_path = base_dir / 'data' / 'input' / 'sample_data.csv'
        file_path = os.getenv('INPUT_FILE', str(default_path))
    
    try:
        print(f"Extracting data from {file_path}")
        data = pd.read_csv(file_path)
        print("Extraction done")
        return data
    except Exception as e:
        print(f"Error during extraction: {e}")
        raise