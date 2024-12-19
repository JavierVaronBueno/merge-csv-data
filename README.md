# CSV Data Processor with Robust Logging and Error Handling

A Python-based script for processing and merging CSV files. This script is designed for data integrators and developers, featuring robust logging, error handling, and flexible file management to streamline data preprocessing tasks.

---

## Features

### 1. **Robust Logging System**
- Generates detailed log files with timestamps for each script execution.
- Logs include information about processed files, missing columns, and errors.
- Helps in debugging and auditing the data processing workflow.

### 2. **File Management**
- Uses **regular expressions (regex)** to identify and process CSV files based on user-defined patterns.
- Handles file naming inconsistencies such as appended numbers (e.g., `file(1).csv`).

### 3. **Data Processing**
- Standardizes column names using a predefined mapping (`COLUMN_MAPPING`).
- Automatically detects and parses date columns.
- Eliminates duplicate rows based on the `Date` column.
- Outputs a merged and cleaned CSV file for each pattern.

### 4. **Error Handling**
- Catches and logs file-specific errors to ensure other files continue processing.
- Warns about missing required columns and skips invalid files gracefully.

---

## System Requirements
- **Python**: 3.7 or higher
- Required Python Libraries:
  - `pandas`
  - `logging`
  - `datetime`
  - `re`

---

## Virtual Environment Setup

### Step 1: Create a Virtual Environment
```bash
# Windows
python -m venv venv

# Linux/Mac
python3 -m venv venv
```

### Step 2: Activate the Virtual Environment
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Step 3: Install Dependencies
1. Create a `requirements.txt` file with the following content:
    ```text
    pandas>=2.0.0
    python-dateutil>=2.8.2
    pytz>=2023.3
    ```
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Script Execution

### Step 1: Directory Structure
Organize your project as follows:
```
project_root/
├── venv/
├── requirements.txt
├── csv_merger.py
└── data/
    └── your_csv_files/
```

### Step 2: Run the Script
```bash
python csv_merger.py
```
- Ensure the environment is activated before running the script.
- Update the `directory` and `patterns` variables in the script to point to your data directory and desired file patterns.

---

## Project Structure
```
project_root/
├── venv/                   # Virtual environment
├── requirements.txt        # Dependencies
├── csv_merger.py           # Main script
├── logs/                   # Log files
├── data/                   # Directory for raw CSV files
└── output/                 # Directory for processed files
```

---

## Example Usage

### Setting Variables
In `csv_merger.py`, set:
- `directory_data` to the path of your CSV files.
- `directory_outpu` to the path where your CSV files are saved.
- `patterns` as a list of base file name patterns. Example:
    ```python
    directory_data = r"c:\Users\TuUsuario\data"
    directory_output = r"c:\Users\TuUsuario\output"
    patterns = ["USD_THB Historical Data", "EUR_USD Historical Data"]
    ```

### Running the Script
1. Activate the virtual environment:
    ```bash
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # Linux/Mac
    ```
2. Run the script:
    ```bash
    python csv_merger.py
    ```

### Output
- A merged CSV file named `<pattern>_TOTAL.csv` will be saved in the `directory` path.
- Detailed logs are stored in the `logs/` folder.

---

## Contributing
We welcome contributions to enhance the project. To contribute:
1. Fork the repository.
2. Create a feature branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes and create a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
For issues, questions, or suggestions:
- **Email**: developer_support@example.com
- **GitHub Issues**: [GitHub Issues](https://github.com/your-repo/issues)
