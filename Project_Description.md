# MITRE ATT&CK Demo - Version 1
This project demonstrates the use of the MITRE ATT&CK framework for understanding cybersecurity threats and techniques. It includes Python scripts for analysing and visualising the ATT&CK data.

## Features

### 1. Fetching MITRE ATT&CK Data
- **Data Source**: The MITRE ATT&CK framework provides a comprehensive matrix of techniques used by adversaries in cybersecurity incidents. This project fetches the data from the MITRE ATT&CK repository.
- **Library Usage**: The project utilizes the `mitreattack` library, which contains modules for fetching and processing ATT&CK data.

### 2. Data Conversion and Storage
- **Data Transformation**: The project converts the fetched ATT&CK data from a DataFrame to a dictionary format suitable for JSON serialization.
- **Storage**: The transformed data is saved as a JSON file, making it easy to access and use later.

### 3. Loading and Displaying Data
- **Data Loading**: The project includes functionality to load the previously saved JSON data.
- **Data Display**: The loaded data is displayed on the command line, listing details of each technique in a readable format.

### 4. Comprehensive Data Attributes
- **Techniques Details**: The project extracts and displays comprehensive attributes for each technique. These attributes provide a detailed overview of each technique's characteristics and usage in cybersecurity incidents.

### 5. Modular Code Structure
- **Script Separation**: The project is divided into two separate scripts for fetching/saving data and loading/displaying data. This modular approach ensures clarity and maintainability.

### 6. Easy Integration and Usage
- **Ease of Use**: The project is designed to be easy to set up and run. Users can follow simple steps to fetch, save, and display the ATT&CK data.

### 7. Readable and Maintainable Code
- **Code Readability**: The code is written in a clear and concise manner, with comments and structured formatting to enhance readability.
- **Maintainability**: The modular approach and clear separation of functionality make the code easy to maintain and extend.

## Coding

### Data Fetching (`fetch_data.py`)
- This script fetches MITRE ATT&CK data, converts it into a JSON format, and saves it into a file.
- **Importing Necessary Libraries**:
  - `mitreattack.attackToExcel.attackToExcel` and `mitreattack.attackToExcel.stixToDf` are modules from the MITRE ATT&CK to Excel library, which provide functions to fetch and process ATT&CK data.
  - `json` is a standard Python library used for handling JSON data.

- **Defining the Function `fetch_and_save_attack_data`**:
  - This function will fetch the MITRE ATT&CK data, process it, and save it as a JSON file.

- **Downloading and Parsing ATT&CK STIX Data**:
  - `attackToExcel.get_stix_data("enterprise-attack")`: Downloads the MITRE ATT&CK data in STIX format.
  - `stixToDf.techniquesToDf(attackdata, "enterprise-attack")`: Converts the STIX data into a DataFrame.
  - `techniques_df = techniques_data["techniques"]`: Extracts the techniques DataFrame from the converted data.

- **Converting DataFrame to Dictionary**:
- `techniques_df.to_dict(orient='records')`: Converts the DataFrame into a list of dictionaries, where each dictionary represents a row in the DataFrame.

- **Saving Dictionary to JSON File**:
  - Opens a file named `data/attack_data.json` in write mode.
  - `json.dump(techniques_dict, json_file, indent=4)`: Writes the dictionary to the JSON file with an indentation of 4 spaces for readability.

- **Main Execution Block**:
  - Ensures the function `fetch_and_save_attack_data()` runs only when the script is executed directly, not when imported as a module.

### Attack Analysis (`attack_analysis.py`)
- This script loads the saved MITRE ATT&CK data from a JSON file and lists all techniques on the command line.

- **Importing the JSON Library**:
  - `json` is a standard Python library used for handling JSON data.

- **Defining the Function `load_and_list_attack_data`**:
  - This function will load the JSON data from the specified file and print the details of each technique.

- **Loading JSON Data from File**:
  - Opens the specified JSON file in read mode.
  - `json.load(json_file)`: Loads the JSON data into a Python list of dictionaries.

- **Listing All Techniques**:
  - Iterates through each technique in the list.
  - Prints each attribute of the technique in a formatted manner. This project prints `ID` and `Name` of the techniques.
  - Adds a separator line (`"-"*80`) between techniques for better readability.

- **Main Execution Block**:
  - Ensures the function `load_and_list_attack_data(json_file_path)` runs only when the script is executed directly, not when imported as a module.
  - Sets the path to the JSON file and calls the function to load and list the data.
