import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def load_data(data, file_path=None):
    """
    Load the transformed data to a destination (CSV in this example)
    """
    if file_path is None:
        file_path = os.getenv('OUTPUT_FILE', '../data/output/processed_data.csv')
    
    try:
        print(f"Loading data to {file_path}")
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Save as CSV
        data.to_csv(file_path, index=False)
        
        print("Data loaded successfully")
        return True
    except Exception as e:
        print(f"Error during loading: {e}")
        raise