# Converter Script

The **Converter Script** is a Python application designed to perform various unit conversions, such as length, temperature, weight, and other measurements. This script provides a simple command-line interface for users to select conversion types and input values to be converted.

## Purpose

The purpose behind creating this script is to enhance Python programming skills by implementing basic functionality for unit conversions. This app was created as part of learning and practicing Python during my data science education at EC Utbildning (2022-2024).

## Flowchart

Below is a flowchart depicting the basic structure, logic, and flow of the converter script:

<img src="docs/unit_converter.svg" alt="Flowchart of Converter Script" width="800" height="600">

## How to Use

1. **Setup**:
   - Ensure Python is installed on your system.
   - Clone or download the script to your local machine.

2. **Run the Script**:
   - Open your terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script using Python:
     ```bash
     python converter.py
     ```

3. **Select Conversion Type**:
   - Choose from the options provided in the main menu:
     ```
     1. Length (meters to feet)
     2. Temperature (Celsius to Fahrenheit)
     3. Weight (kilograms to pounds)
     4. Other (liters to gallons)
     5. Exit
     ```

4. **Enter Value to Convert**:
   - Input the value you want to convert when prompted.
   - The script will display the converted value along with the conversion details.

5. **Exit the Script**:
   - Choose the option to exit from the main menu to close the application.

## Requirements

- Python 3.x

## Features

- Converts units of length, temperature, weight, and other measurements.
- User-friendly command-line interface.
- Provides error handling for invalid inputs.

## Conversion Factors

- **Length**: Meters to Feet (1 meter = 3.28084 feet)
- **Temperature**: Celsius to Fahrenheit (°F = °C * 9/5 + 32)
- **Weight**: Kilograms to Pounds (1 kilogram = 2.20462 pounds)
- **Other**: Liters to Gallons (1 liter = 0.264172 gallons)

## Example Usage

```bash
python converter.py

1. Select Conversion Type
2. Exit

Please select what you wish to do:
1

1. Length (meters to feet)
2. Temperature (Celsius to Fahrenheit)
3. Weight (kilograms to pounds)
4. Other

Please select conversion type:
2

Enter value to convert:
25
Converted value: 25°C is 77.0°F
