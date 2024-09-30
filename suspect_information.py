import random
from save import Save
import json

class SuspectInformation:
    suspect_hair_color_list = ['blue', 'black', 'brown', 'golden', 'brunette'] # specifies different hair colors that that suspect can have
    suspect_height_type_list = ['short', 'tall'] # specifies whether the suspect is short or tall
    suspect_blood_type_list = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'] # specifies the suspect's blood type
    suspect_eye_color_list = ['black', 'brown', 'red', 'hazel', 'grey', 'blue'] # specifies the suspect's eye color
    suspect_ethnicity_list = ['Asian', 'Indian', 'African', 'American', 'European'] # specifies the suspect's ethnicity
    
    # dictionary to hold the different colors the suspect can be, according to their ethnicity
    suspect_skin_color_dict = {
        'Asian': ['light'],
        'Indian': ['light', 'dark', 'olive'],
        'African': ['dark'],
        'American': ['light'],
        'European': ['olive', 'white', 'caucasian']
    }
    
    # following function generate values for reports for each of the 5 suspects in the suspects list
    def generate_suspect_report_values(suspect_1_name, suspect_2_name, suspect_3_name, suspect_4_name, suspect_5_name, hair_color_1, hair_color_2, hair_color_3, hair_color_4, hair_color_5, height_type_1, height_type_2, height_type_3, height_type_4, height_type_5, blood_type_1, blood_type_2, blood_type_3, blood_type_4, blood_type_5, eye_color_1, eye_color_2, eye_color_3, eye_color_4, eye_color_5, ethnicity_1, ethnicity_2, ethnicity_3, ethnicity_4, ethnicity_5, skin_color_1, skin_color_2, skin_color_3, skin_color_4, skin_color_5, save = True):
        suspect_components = {
            'suspect 1 name': suspect_1_name,
            'hair 1': hair_color_1,
            'height type 1': height_type_1,
            'blood type 1': blood_type_1,
            'skin color 1': skin_color_1,
            'eye color 1': eye_color_1,
            'ethnicity 1': ethnicity_1,
            
            'suspect 2 name': suspect_2_name,
            'hair 2': hair_color_2,
            'height type 2': height_type_2,
            'blood type 2': blood_type_2,
            'skin color 2': skin_color_2,
            'eye color 2': eye_color_2,
            'ethnicity 2': ethnicity_2,
            
            'suspect 3 name': suspect_3_name,
            'hair 3': hair_color_3,
            'height type 3': height_type_3,
            'blood type 3': blood_type_3,
            'skin color 3': skin_color_3,
            'eye color 3': eye_color_3,
            'ethnicity 3': ethnicity_3,
            
            'suspect 4 name': suspect_4_name,
            'hair 4': hair_color_4,
            'height type 4': height_type_4,
            'blood type 4': blood_type_4,
            'skin color 4': skin_color_4,
            'eye color 4': eye_color_4,
            'ethnicity 4': ethnicity_4,
            
            'suspect 5 name': suspect_5_name,
            'hair 5': hair_color_5,
            'height type 5': height_type_5,
            'blood type 5': blood_type_5,
            'skin color 5': skin_color_5,
            'eye color 5': eye_color_5,
            'ethnicity 5': ethnicity_5,
        }
        
        if save:
            Save.save_suspects_info(suspect_components)
            
        return suspect_components
    
    # following functions generate a report file for the detective to read on all the present suspects
    def generate_suspect_1_report(suspect_1, hair_color, height_type, blood_type, eye_color, ethnicity, skin_color, save = True):
        suspect_1_report = f'{suspect_1} is a {hair_color} haired {height_type} individual\nwith a {blood_type} blood group. Suspect is {skin_color} toned, with {eye_color} eyes and is {ethnicity}'
        
        if save:
            Save.save_suspect_1_info_file(suspect_1_report)

        print(suspect_1_report)
        return suspect_1_report
    
    def read_suspect_1_report():
        with open('suspects 1 information file.json', 'r') as json_file:
            suspect_1_report_data = json.load(json_file)
          
        return suspect_1_report_data
    
    def generate_suspect_2_report(suspect_2, hair_color, height_type, blood_type, eye_color, ethnicity, skin_color, save = True):
        suspect_2_report = f'{suspect_2} is a {hair_color} haired {height_type} individual\nwith a {blood_type} blood group. Suspect is {skin_color} toned, with {eye_color} eyes and is {ethnicity}'
        
        if save:
            Save.save_suspect_2_info_file(suspect_2_report)
        
        print(suspect_2_report)
        return suspect_2_report
    
    def read_suspect_2_report():
        with open('suspects 2 information file.json', 'r') as json_file:
            suspect_2_report_data = json.load(json_file)
          
        return suspect_2_report_data
    
    def generate_suspect_3_report(suspect_3, hair_color, height_type, blood_type, eye_color, ethnicity, skin_color, save = True):
        suspect_3_report = f'{suspect_3} is a {hair_color} haired {height_type} individual\nwith a {blood_type} blood group. Suspect is {skin_color} toned, with {eye_color} eyes and is {ethnicity}'
        
        if save:
            Save.save_suspect_3_info_file(suspect_3_report)
        
        print(suspect_3_report)
        return suspect_3_report
    
    def read_suspect_3_report():
        with open('suspects 3 information file.json', 'r') as json_file:
            suspect_3_report_data = json.load(json_file)
          
        return suspect_3_report_data
    
    def generate_suspect_4_report(suspect_4, hair_color, height_type, blood_type, eye_color, ethnicity, skin_color, save = True):
        suspect_4_report = f'{suspect_4} is a {hair_color} haired {height_type} individual\nwith a {blood_type} blood group. Suspect is {skin_color} toned, with {eye_color} eyes and is {ethnicity}'
        
        if save:
            Save.save_suspect_4_info_file(suspect_4_report)
        
        print(suspect_4_report)
        return suspect_4_report
    
    def read_suspect_4_report():
        with open('suspects 4 information file.json', 'r') as json_file:
            suspect_4_report_data = json.load(json_file)
  
        return suspect_4_report_data
    
    def generate_suspect_5_report(suspect_5, hair_color, height_type, blood_type, eye_color, ethnicity, skin_color, save = True):
        suspect_5_report = f'{suspect_5} is a {hair_color} haired {height_type} individual\nwith a {blood_type} blood group. Suspect is {skin_color} toned, with {eye_color} eyes and is {ethnicity}'
        
        if save:
            Save.save_suspect_5_info_file(suspect_5_report)
        
        print(suspect_5_report)
        return suspect_5_report
    
    def read_suspect_5_report():
        with open('suspects 5 information file.json', 'r') as json_file:
            suspect_5_report_data = json.load(json_file)
         
        return suspect_5_report_data
    
    
    # generates the different features of the suspects to be passed into the generate suspect report methods
    def get_hair_color(possible_hair_colors):
        hair_color = random.choice(possible_hair_colors)
        
        return hair_color
    
    def get_height_type(possible_height_types):
        height_type = random.choice(possible_height_types)
        
        return height_type
    
    def get_blood_type(possible_blood_types):
        blood_type = random.choice(possible_blood_types)
        
        return blood_type
    
    def get_eye_color(possible_eye_colors):
        eye_color = random.choice(possible_eye_colors)
        
        return eye_color
    
    def get_suspect_ethnicity(possible_ethnicity_types):
        suspect_ethnicity = random.choice(possible_ethnicity_types)
        
        return suspect_ethnicity
    
    def suspect_skin_color(ethnicity, possible_skin_colors):
        if ethnicity in possible_skin_colors:
            skin_color = random.choice(possible_skin_colors[ethnicity])
            
        return skin_color
    
    # calls all the methods responsible for creating suspect information presentable to the detective
    def generate_all_suspects_information():
        suspects_report_values_file = 'suspects info.json'
        case_data_file = 'case data.json'
        
        print('')
        
        with open(case_data_file, 'r') as json_file:
            case_data = json.load(json_file)
            
        suspect_list = case_data.get('selected suspects')
        
        # suspect 1
        selected_hair_color_1 = SuspectInformation.get_hair_color(SuspectInformation.suspect_hair_color_list)
        selected_height_type_1 = SuspectInformation.get_height_type(SuspectInformation.suspect_height_type_list)
        selected_blood_type_1 = SuspectInformation.get_blood_type(SuspectInformation.suspect_blood_type_list)
        selected_eye_color_1 = SuspectInformation.get_eye_color(SuspectInformation.suspect_eye_color_list)
        selected_ethnicity_1 = SuspectInformation.get_suspect_ethnicity(SuspectInformation.suspect_ethnicity_list)
        selected_skin_color_1 = SuspectInformation.suspect_skin_color(selected_ethnicity_1, SuspectInformation.suspect_skin_color_dict)
        
        # suspect 2
        selected_hair_color_2 = SuspectInformation.get_hair_color(SuspectInformation.suspect_hair_color_list)
        selected_height_type_2 = SuspectInformation.get_height_type(SuspectInformation.suspect_height_type_list)
        selected_blood_type_2 = SuspectInformation.get_blood_type(SuspectInformation.suspect_blood_type_list)
        selected_eye_color_2 = SuspectInformation.get_eye_color(SuspectInformation.suspect_eye_color_list)
        selected_ethnicity_2 = SuspectInformation.get_suspect_ethnicity(SuspectInformation.suspect_ethnicity_list)
        selected_skin_color_2 = SuspectInformation.suspect_skin_color(selected_ethnicity_2, SuspectInformation.suspect_skin_color_dict)
        
        # suspect 3
        selected_hair_color_3 = SuspectInformation.get_hair_color(SuspectInformation.suspect_hair_color_list)
        selected_height_type_3 = SuspectInformation.get_height_type(SuspectInformation.suspect_height_type_list)
        selected_blood_type_3 = SuspectInformation.get_blood_type(SuspectInformation.suspect_blood_type_list)
        selected_eye_color_3 = SuspectInformation.get_eye_color(SuspectInformation.suspect_eye_color_list)
        selected_ethnicity_3 = SuspectInformation.get_suspect_ethnicity(SuspectInformation.suspect_ethnicity_list)
        selected_skin_color_3 = SuspectInformation.suspect_skin_color(selected_ethnicity_3, SuspectInformation.suspect_skin_color_dict)
        
        # suspect 4
        selected_hair_color_4 = SuspectInformation.get_hair_color(SuspectInformation.suspect_hair_color_list)
        selected_height_type_4 = SuspectInformation.get_height_type(SuspectInformation.suspect_height_type_list)
        selected_blood_type_4 = SuspectInformation.get_blood_type(SuspectInformation.suspect_blood_type_list)
        selected_eye_color_4 = SuspectInformation.get_eye_color(SuspectInformation.suspect_eye_color_list)
        selected_ethnicity_4 = SuspectInformation.get_suspect_ethnicity(SuspectInformation.suspect_ethnicity_list)
        selected_skin_color_4 = SuspectInformation.suspect_skin_color(selected_ethnicity_4, SuspectInformation.suspect_skin_color_dict)
        
        # suspect 5
        selected_hair_color_5 = SuspectInformation.get_hair_color(SuspectInformation.suspect_hair_color_list)
        selected_height_type_5 = SuspectInformation.get_height_type(SuspectInformation.suspect_height_type_list)
        selected_blood_type_5 = SuspectInformation.get_blood_type(SuspectInformation.suspect_blood_type_list)
        selected_eye_color_5 = SuspectInformation.get_eye_color(SuspectInformation.suspect_eye_color_list)
        selected_ethnicity_5 = SuspectInformation.get_suspect_ethnicity(SuspectInformation.suspect_ethnicity_list)
        selected_skin_color_5 = SuspectInformation.suspect_skin_color(selected_ethnicity_5, SuspectInformation.suspect_skin_color_dict)
        
        SuspectInformation.generate_suspect_report_values(suspect_list[0], suspect_list[1], suspect_list[2], suspect_list[3], suspect_list[4], selected_hair_color_1, selected_hair_color_2, selected_hair_color_3, selected_hair_color_4, selected_hair_color_5, selected_height_type_1, selected_height_type_2, selected_height_type_3, selected_height_type_4, selected_height_type_5, selected_blood_type_1, selected_blood_type_2, selected_blood_type_3, selected_blood_type_4, selected_blood_type_5, selected_eye_color_1, selected_eye_color_2, selected_eye_color_3, selected_eye_color_4, selected_eye_color_5, selected_ethnicity_1, selected_ethnicity_2, selected_ethnicity_3, selected_ethnicity_4, selected_ethnicity_5, selected_skin_color_1, selected_skin_color_2, selected_skin_color_3, selected_skin_color_4, selected_skin_color_5)
        
        with open(suspects_report_values_file, 'r') as json_file:
            suspects_info = json.load(json_file)
            
        # pulls saved suspect data from the suspects info.json
        # suspect 1
        pulled_suspect_1_name = suspect_list[0]
        pulled_suspect_1_hair_color = suspects_info.get('hair 1')
        pulled_suspect_1_height_type = suspects_info.get('height type 1')
        pulled_suspect_1_blood_type = suspects_info.get('blood type 1')
        pulled_suspect_1_eye_color = suspects_info.get('eye color 1')
        pulled_suspect_1_ethnicity = suspects_info.get('ethnicity 1')
        pulled_suspect_1_skin_color = suspects_info.get('skin color 1')
        
        # suspect 2
        pulled_suspect_2_name = suspect_list[1]
        pulled_suspect_2_hair_color = suspects_info.get('hair 2')
        pulled_suspect_2_height_type = suspects_info.get('height type 2')
        pulled_suspect_2_blood_type = suspects_info.get('blood type 2')
        pulled_suspect_2_eye_color = suspects_info.get('eye color 2')
        pulled_suspect_2_ethnicity = suspects_info.get('ethnicity 2')
        pulled_suspect_2_skin_color = suspects_info.get('skin color 2')
        
        # suspect 3
        pulled_suspect_3_name = suspect_list[2]
        pulled_suspect_3_hair_color = suspects_info.get('hair 3')
        pulled_suspect_3_height_type = suspects_info.get('height type 3')
        pulled_suspect_3_blood_type = suspects_info.get('blood type 3')
        pulled_suspect_3_eye_color = suspects_info.get('eye color 3')
        pulled_suspect_3_ethnicity = suspects_info.get('ethnicity 3')
        pulled_suspect_3_skin_color = suspects_info.get('skin color 3')
        
        # suspect 4
        pulled_suspect_4_name = suspect_list[3]
        pulled_suspect_4_hair_color = suspects_info.get('hair 4')
        pulled_suspect_4_height_type = suspects_info.get('height type 4')
        pulled_suspect_4_blood_type = suspects_info.get('blood type 4')
        pulled_suspect_4_eye_color = suspects_info.get('eye color 4')
        pulled_suspect_4_ethnicity = suspects_info.get('ethnicity 4')
        pulled_suspect_4_skin_color = suspects_info.get('skin color 4')
        
        # suspect 5
        pulled_suspect_5_name = suspect_list[4]
        pulled_suspect_5_hair_color = suspects_info.get('hair 5')
        pulled_suspect_5_height_type = suspects_info.get('height type 5')
        pulled_suspect_5_blood_type = suspects_info.get('blood type 5')
        pulled_suspect_5_eye_color = suspects_info.get('eye color 5')
        pulled_suspect_5_ethnicity = suspects_info.get('ethnicity 5')
        pulled_suspect_5_skin_color = suspects_info.get('skin color 5')
        
        SuspectInformation.generate_suspect_1_report(pulled_suspect_1_name, pulled_suspect_1_hair_color, pulled_suspect_1_height_type, pulled_suspect_1_blood_type, pulled_suspect_1_eye_color, pulled_suspect_1_ethnicity, pulled_suspect_1_skin_color)
        print('')
        SuspectInformation.generate_suspect_2_report(pulled_suspect_2_name, pulled_suspect_2_hair_color, pulled_suspect_2_height_type, pulled_suspect_2_blood_type, pulled_suspect_2_eye_color, pulled_suspect_2_ethnicity, pulled_suspect_2_skin_color)
        print('')
        SuspectInformation.generate_suspect_3_report(pulled_suspect_3_name, pulled_suspect_3_hair_color, pulled_suspect_3_height_type, pulled_suspect_3_blood_type, pulled_suspect_3_eye_color, pulled_suspect_3_ethnicity, pulled_suspect_3_skin_color)
        print('')
        SuspectInformation.generate_suspect_4_report(pulled_suspect_4_name, pulled_suspect_4_hair_color, pulled_suspect_4_height_type, pulled_suspect_4_blood_type, pulled_suspect_4_eye_color, pulled_suspect_4_ethnicity, pulled_suspect_4_skin_color)
        print('')
        SuspectInformation.generate_suspect_5_report(pulled_suspect_5_name, pulled_suspect_5_hair_color, pulled_suspect_5_height_type, pulled_suspect_5_blood_type, pulled_suspect_5_eye_color, pulled_suspect_5_ethnicity, pulled_suspect_5_skin_color)
        print('')
