import mitreattack.attackToExcel.attackToExcel as attackToExcel
import mitreattack.attackToExcel.stixToDf as stixToDf
import json

def fetch_and_save_attack_data():
    
    print("Fetching MITRE ATT&CK data...")
    
    # download and parse ATT&CK STIX data
    attackdata = attackToExcel.get_stix_data("enterprise-attack")
    techniques_data = stixToDf.techniquesToDf(attackdata, "enterprise-attack")
    techniques_df = techniques_data["techniques"]
    
    # Convert DataFrame to dictionary
    techniques_dict = techniques_df.to_dict(orient='records')
    
    # Save dictionary to JSON file
    with open('data/attack_data.json', 'w') as json_file:
        json.dump(techniques_dict, json_file, indent=4)
       
    print("Data fetched and saved to data/attack_data.json") 
        
if __name__ == "__main__":
    fetch_and_save_attack_data()
    
