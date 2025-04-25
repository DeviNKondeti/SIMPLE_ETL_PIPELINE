from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def run_pipeline(input_file=None, output_file=None):
    """
    Run the complete ETL pipeline
    """
    try:
        print("Starting ETL Pipeline")
        
        # Extract
        raw_data = extract_data(input_file)
        
        # Transform
        processed_data = transform_data(raw_data)
        
        # Load
        load_data(processed_data, output_file)
        
        print("ETL Pipeline completed successfully")
        return True
    except Exception as e:
        print(f"Pipeline failed: {e}")
        return False

if __name__ == "__main__":
    run_pipeline()