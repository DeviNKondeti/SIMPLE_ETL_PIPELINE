import pandas as pd

def transform_data(data):
    """
    Perform transformations on the extracted data
    """
    try:
        print("Starting transformation")
        
        # Example transformations:
        # 1. Clean data - remove nulls
        transformed = data.dropna()
        
        # 2. Standardize text columns (example: convert names to title case)
        if 'name' in transformed.columns:
            transformed['name'] = transformed['name'].str.title()
            
        # 3. Create derived columns (example: combine first and last name)
        if all(col in transformed.columns for col in ['first_name', 'last_name']):
            transformed['full_name'] = transformed['first_name'] + ' ' + transformed['last_name']
        
        print("Transformation complete")
        return transformed
    except Exception as e:
        print(f"Error during transformation: {e}")
        raise