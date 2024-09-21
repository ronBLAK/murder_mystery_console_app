import json

class SaveCaseInfo:
    
    def save_case(case_to_save):
        file_path = 'case info.json'
        
        with open(file_path, 'w') as json_file:
            json.dump(case_to_save, json_file, indent= 4)
            
    def save_case_file(case_file_to_save):
        file_path = 'case file.json'
        
        with open(file_path, 'w') as json_file:
            json.dump(case_file_to_save, json_file, indent= 4)