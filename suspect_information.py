from case_gen import CaseGen
import json

class SuspectInformation:
    file_path = 'case data.json'
    
    with open(file_path, 'r') as json_file:
        case_data = json.load(json_file)
    
    suspects_list = case_data.get('selected suspects')
    culprit = case_data.get('culprit name')
    
    def generate_suspect_1_report(suspects):
        suspect_1_report = f'{suspects[0]} is one of the suspects.'
        
        return suspect_1_report
    
    def generate_suspect_2_report(suspects):
        suspect_2_report = f'{suspects[1]} is one of the suspects.'
        
        return suspect_2_report
    
    def generate_suspect_3_report(suspects):
        suspect_3_report = f'{suspects[2]} is one of the suspects.'
        
        return suspect_3_report
    
    def generate_suspect_4_report(suspects):
        suspect_4_report = f'{suspects[3]} is one of the suspects.'
                
        return suspect_4_report
    
    def generate_suspect_5_report(suspects):
        suspect_5_report = f'{suspects[4]} is one of the suspects.'
        
        return suspect_5_report