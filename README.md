
# Streamlit Calculator Application

## Overview
This is a basic calculator application built using **Streamlit**. It provides an interactive UI for users to perform arithmetic operations such as addition, subtraction, multiplication, and division.

## Features
- **Interactive Web-Based Calculator**
- Perform basic arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division (with division-by-zero handling)
- Simple and intuitive user interface.

## How to Use
1. **Input Numbers**:
   - Enter two numbers using the number input fields.
2. **Select an Operation**:
   - Choose the desired arithmetic operation from the dropdown menu.
3. **Calculate the Result**:
   - Click the "Calculate" button to view the result.

## Requirements
- Python 3.7 or higher
- Streamlit library

## Installation
1. Install Streamlit by running:
   ```bash
   pip install streamlit
   ```
2. Save the script as `calculator_app.py`.

## Running the Application
1. Open a terminal or command prompt.
2. Navigate to the folder containing the `calculator_app.py` file.
3. Run the application using:
   ```bash
   streamlit run calculator_app.py
   ```
4. Open the provided URL (e.g., `http://localhost:8501`) in your browser to use the app.

## Example
### Input:
- **1st Number**: 15
- **2nd Number**: 3
- **Operation**: Multiplication (*)

### Output:
- **Result**: 45

## Notes
- For division, the application prevents division by zero and displays an appropriate error message.
- Ensure that both numbers are entered before performing the calculation.

## License
This application is open-source and free to use.
