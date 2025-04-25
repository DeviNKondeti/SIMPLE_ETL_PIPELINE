# Simple ETL Pipeline Project

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/pandas-1.0%2B-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

A complete Python implementation of a basic ETL (Extract, Transform, Load) pipeline with modular design and environment configuration.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Modules Documentation](#modules-documentation)
7. [Sample Data](#sample-data)
8. [Contributing](#contributing)
9. [License](#license)

## Project Overview

This ETL pipeline demonstrates:
- **Extract**: Reading data from CSV files
- **Transform**: Cleaning and processing data (handling missing values, formatting)
- **Load**: Saving processed data to new CSV files

Key Features:
- Environment variable configuration
- Modular architecture
- Error handling
- Sample dataset included

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/DeviNKondeti/SIMPLE_ETL_PIPELINE.git
   cd SIMPLE_ETL_PIPELINE
   ```

2. Create and activate virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create `.env` file in project root:
   ```ini
   # Paths are relative to project root
   INPUT_FILE=data/input/sample_data.csv
   OUTPUT_FILE=data/output/processed_data.csv
   ```

2. Place your input files in `data/input/` directory

## Usage

### Running the Pipeline
```bash
python main.py
```

### Expected Output
1. Processed data will be saved to `data/output/processed_data.csv`
2. Console will show progress:
   ```
   Starting ETL Pipeline
   Extracting data from data/input/sample_data.csv
   Extraction complete
   Starting transformation
   Transformation complete
   Loading data to data/output/processed_data.csv
   Data loaded successfully
   ETL Pipeline completed successfully
   ```

## Project Structure

```
ETL_pipeline/
├── data/                   # Data directory
│   ├── input/              # Input data (git-ignored)
│   └── output/             # Output data (git-ignored)
├── etl/                   
