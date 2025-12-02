import random
from save import Save
import json

class Suspects:
    suspect_hair_color_list = ['blue', 'black', 'blonde', 'brunette', 'red', 'ginger', 'grey', 'white'] # specifies different hair colors that that suspect can have
    suspect_height_type_list = ['short', 'tall'] # specifies whether the suspect is short or tall
    suspect_blood_type_list = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'] # specifies the suspect's blood type
    suspect_eye_color_list = ['black', 'brown', 'red', 'hazel', 'grey', 'blue'] # specifies the suspect's eye color
    suspect_ethnicity_list = ['Asian', 'Indian', 'African', 'American', 'European'] # specifies the suspect's ethnicity
    
    # dictionary to hold the different colors the suspect can be, according to their ethnicity
    suspect_skin_color_dict = {
        'Asian': ['light', 'olive'],
        'Indian': ['light', 'dark', 'olive'],
        'African': ['dark', 'light'],
        'American': ['light', 'dark', 'olive'],
        'European': ['olive', 'white', 'caucasian']
    }
    
    # generate the suspects data, just like the case data
    def generate_suspect_values(suspect_name, hair_color, height_type, blood_type, eye_color, ethnicity, skin_color, save = True):
        # all the variables this functions needs to function - the lists and other derived values
        suspects_info = {
            'suspect names': suspect_name,
            'hair colors': hair_color,
            'height types': height_type,
            'blood types': blood_type,
            'eye colors': eye_color,
            'ethinicity': ethnicity,
            'skin colors': skin_color
        }
        
        if save:
            Save.save_suspects_info(suspects_info)
            
        return suspects_info
    
    def generate_suspect_report(suspect_number, suspect_name, hair_color, height_type, blood_type, eye_color, ethnicity, skin_color, save = True):
        suspect_report_list = []
        
        for suspect in range(suspect_number):
            suspect_report = f'The {suspect_name[suspect]} is a {hair_color[suspect]} haired {height_type[suspect]} individual\nwith a {blood_type[suspect]} blood group. Suspect is {skin_color[suspect]} toned, with {eye_color[suspect]} eyes and is {ethnicity[suspect]}'
            
            suspect_report_list.append(suspect_report)
            
        if save:
            Save.save_suspects_file(suspect_report_list)
            
    def read_suspect_report():
        with open('suspects file.json', 'r') as json_file:
            suspect_report_data = json.load(json_file)
            
        return suspect_report_data
    
    # generates the different features of the suspects to be passed into the generate suspect report methods
    def get_hair_color(possible_hair_colors, suspect_number):
        hair_color_list = []
        
        for _ in range(suspect_number):
            hair_color = random.choice(possible_hair_colors)
            hair_color_list.append(hair_color)
        
        return hair_color_list
    
    def get_height_type(possible_height_types, suspect_number):
        height_type_list = []
        
        for _ in range(suspect_number):
            height_type = random.choice(possible_height_types)
            height_type_list.append(height_type)
        
        return height_type_list
    
    def get_blood_type(possible_blood_types, suspect_number):
        blood_type_list = []
        
        for _ in range(suspect_number):
            blood_type = random.choice(possible_blood_types)
            blood_type_list.append(blood_type)
        
        return blood_type_list
    
    def get_eye_color(possible_eye_colors, suspect_number):
        eye_color_list = []
        
        for _ in range(suspect_number):
            eye_color = random.choice(possible_eye_colors)
            eye_color_list.append(eye_color)
        
        return eye_color_list
    
    def get_suspect_ethnicity(possible_ethnicity_types, suspect_number):
        suspect_ethnicity_list = []
        
        for _ in range(suspect_number):
            suspect_ethnicity = random.choice(possible_ethnicity_types)
            suspect_ethnicity_list.append(suspect_ethnicity)
        
        return suspect_ethnicity_list
    
    def get_skin_color(ethnicity, possible_skin_colors, suspect_number):
        skin_color_list = []
        
        for i in range(suspect_number):
            if ethnicity[i] in possible_skin_colors:
                skin_color = random.choice(possible_skin_colors[ethnicity[i]])
                skin_color_list.append(skin_color)
            
        return skin_color_list
    
    # brings the two generate functions decalared above, from one function, which is declared below
    def generate_suspects_report_random():
        suspects_report_values_file = 'suspects info.json'
        
        with open('case data.json', 'r') as file:
            case_data = json.load(file)
                
        suspect_names = case_data['case details']['selected suspects']
        
        # sets each of the derived values into its own variable to use in the first generate method, and save the data
        selected_hair_colors = Suspects.get_hair_color(Suspects.suspect_hair_color_list, 5)
        selected_height_types = Suspects.get_height_type(Suspects.suspect_height_type_list, 5)
        selected_blood_types = Suspects.get_blood_type(Suspects.suspect_blood_type_list, 5)
        selected_eye_color = Suspects.get_eye_color(Suspects.suspect_eye_color_list, 5)
        selected_ethnicity = Suspects.get_suspect_ethnicity(Suspects.suspect_ethnicity_list, 5)
        selected_skin_color = Suspects.get_skin_color(selected_ethnicity, Suspects.suspect_skin_color_dict, 5)
        
        Suspects.generate_suspect_values(suspect_names, selected_hair_colors, selected_height_types, selected_blood_types, selected_eye_color, selected_ethnicity, selected_skin_color)
        
        # retrieves the saved values, thanks to the previous method, and use those values to generate the actual report
        with open(suspects_report_values_file, 'r') as json_file:
            suspect_info = json.load(json_file)
            
        pulled_hair_colors = suspect_info.get('hair colors')
        pulled_height_types = suspect_info.get('height types')
        pulled_blood_types = suspect_info.get('blood types')
        pulled_eye_colors = suspect_info.get('eye colors')
        pulled_ethnicity = suspect_info.get('ethinicity')
        pulled_skin_color = suspect_info.get('skin colors')
        
        Suspects.generate_suspect_report(5, suspect_names, pulled_hair_colors, pulled_height_types, pulled_blood_types, pulled_eye_colors, pulled_ethnicity, pulled_skin_color)