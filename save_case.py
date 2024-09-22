import json

class Save:
    
    # used to save the case data
    def save_case(case_to_save):
        file_path = 'case data.json'
        
        with open(file_path, 'w') as json_file:
            json.dump(case_to_save, json_file, indent= 4)
            
    # used to save the case file presented to the detective
    def save_case_file(case_file_to_save):
        file_path = 'case file.json'
        
        with open(file_path, 'w') as json_file:
            json.dump(case_file_to_save, json_file, indent= 4)
        
    # used to save all information regarding the detective (name, cases solved, accuracy etc)    
    def save_detective(dective_info):
        file_path = 'detective data.json'
        
        with open(file_path, 'w') as json_file:
            json.dump(dective_info, json_file, indent= 4)
