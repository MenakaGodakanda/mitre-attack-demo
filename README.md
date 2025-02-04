# MITRE ATT&CK Demo
This project demonstrates the use of the MITRE ATT&CK framework for understanding cybersecurity threats and techniques. It includes Python scripts for analysing and visualising the ATT&CK data.<br>
<a href="https://github.com/MenakaGodakanda/mitre-attack-demo/blob/main/Project_Description.md">Project Description</a>

## Overview
<img width="923" alt="Screenshot 2024-07-31 at 5 08 50 AM" src="https://github.com/user-attachments/assets/d72059c3-ab33-47ae-b027-7e0906cd8a87">

### Explanation
#### 1. MITRE ATT&CK Framework Data Source:
- The source of data fetched using the `mitreattack-python` library.

#### 2. Data Fetching:
- **fetch_data.py**: Fetches MITRE ATT&CK data using the `mitreattack-python` library and saves it to `attack_data.json`.

#### 3. Attack Analysis:
- **attack_analysis.py**: Analyse MITRE ATT&CK data using the `attack_data.json`.

## Setup Instructions

### 1. Clone the repository:
   ```sh
   git clone https://github.com/MenakaGodakanda/mitre-attack-demo.git
   cd mitre_attack_demo
   ```

### 2. Install Required Tools and Libraries:
- **Python**: Programming language for scripting. 
```sh
sudo apt install python3 python3-pip
```
- **venv**: Create lightweight `virtual environments`.
```sh
sudo apt install python3-venv
```
- **mitreattack-python**: `mitreattack-python` is a library of Python tools and utilities for working with ATT&CK content.
```
pip install mitreattack-python
```

### 3. Set Up a Virtual Environment:
  ```sh
  python3 -m venv venv
  source venv/bin/activate
  ```

### 4. Fetch MITRE ATT&CK Data:
  ```sh
  python scripts/fetch_data.py
  ```
- This script will download the MITRE ATT&CK data and save it to `data/attack_data.json`. The output in the terminal should look like this:<br>
![Screenshot 2024-07-31 033945](https://github.com/user-attachments/assets/05c6e720-7a03-495b-b349-52f8a9e2daab)

- Verify that the JSON file is created in the data directory:<br>
![Screenshot 2024-07-31 041725](https://github.com/user-attachments/assets/c8cc2562-4a46-4116-af43-8e7dc9ac23a5)


### 5. Run the Attack Analysis:
  ```sh
  python scripts/attack_analysis.py
  ```
- This script will print a list of techniques from the MITRE ATT&CK framework. The output in the terminal should look like this:<br>
![Screenshot 2024-07-31 145754](https://github.com/user-attachments/assets/a40448ee-8f64-4faf-b5a5-867a0188ff50)
- `attack_analysis.py` script is constructured to print all the details of techniques. For demonstration, this project only print `ID` and `Name` of the Techniques.
## Project Structure
```
mitre_attack_demo/
├── venv/                 # Virtual environment
├── data/                 # Directory for storing data files
│ └── attack_data.json
├── scripts/              # Directory for scripts
│ ├── fetch_data.py       # Script to fetch MITRE ATT&CK data
│ └── attack_analysis.py  # Script to analyse attack techniques
└── README.md             # Project documentation
```

## License
This project is licensed under the MIT License.
