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
            
    def save_suspects_info(suspects_info):
        file_path = 'suspects info.json'
        
        with open(file_path, 'w') as json_file:
            json.dump(suspects_info, json_file, indent= 4)
            
            
    # the following methosds save each suspect information for the detective in its own file        
    def save_suspect_1_info_file(suspects_info_file):
        file_path = 'suspects 1 information file.json'
        
        with open(file_path, 'w') as json_file:
            json.dump(suspects_info_file, json_file, indent= 4)
            
    def save_suspect_2_info_file(suspects_info_file):
        file_path = 'suspects 2 information file.json'
        
        with open(file_path, 'w') as json_file:
            json.dump(suspects_info_file, json_file, indent= 4)
            
    def save_suspect_3_info_file(suspects_info_file):
        file_path = 'suspects 3 information file.json'
        
        with open(file_path, 'w') as json_file:
            json.dump(suspects_info_file, json_file, indent= 4)
            
    def save_suspect_4_info_file(suspects_info_file):
        file_path = 'suspects 4 information file.json'
        
        with open(file_path, 'w') as json_file:
            json.dump(suspects_info_file, json_file, indent= 4)
            
    def save_suspect_5_info_file(suspects_info_file):
        file_path = 'suspects 5 information file.json'
        
        with open(file_path, 'w') as json_file:
            json.dump(suspects_info_file, json_file, indent= 4)
