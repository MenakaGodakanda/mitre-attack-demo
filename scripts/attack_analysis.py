import json

def load_and_list_attack_data(json_file_path):
    # Load JSON data from file
    with open(json_file_path, 'r') as json_file:
        techniques_data = json.load(json_file)
    
    # List all techniques
    for technique in techniques_data:
        print(f"ID: {technique['ID']}")
        # print(f"STIX ID: {technique['STIX ID']}")
        print(f"Name: {technique['name']}")
        # print(f"Description: {technique['description']}")
        # print(f"URL: {technique['url']}")
        # print(f"Created: {technique['created']}")
        # print(f"Last Modified: {technique['last modified']}")
        # print(f"Domain: {technique['domain']}")
        # print(f"Version: {technique['version']}")
        # print(f"Tactics: {technique['tactics']}")
        # print(f"Detection: {technique['detection']}")
        # print(f"Platforms: {technique['platforms']}")
        # print(f"Data Sources: {technique['data sources']}")
        # print(f"Is Sub-Technique: {technique['is sub-technique']}")
        # print(f"Sub-Technique Of: {technique['sub-technique of']}")
        # print(f"Defenses Bypassed: {technique['defenses bypassed']}")
        # print(f"Contributors: {technique['contributors']}")
        # print(f"Permissions Required: {technique['permissions required']}")
        # print(f"Supports Remote: {technique['supports remote']}")
        # print(f"System Requirements: {technique['system requirements']}")
        # print(f"Impact Type: {technique['impact type']}")
        # print(f"Effective Permissions: {technique['effective permissions']}")
        # print(f"Relationship Citations: {technique['relationship citations']}")
        print("\n" + "-"*80 + "\n")

if __name__ == "__main__":
    json_file_path = 'data/attack_data.json'  # Path to your JSON file
    load_and_list_attack_data(json_file_path)
