import random
from save import Save
import json
from case_gen import CaseGen

class WitnessGen:
    witness_mode_of_perception = ['saw', 'heard'] # holds different actions that the witness could be produced for witnessing (i.e 'saw' the murder taking place OR 'heard' the gunshots of the murder)
    
    # event they percieved
    event_witnessed_dict = {
        'saw': ['the killer running away', 'the act of murder, but not the killer', 'the body of victim being disposed'],
        'heard': ['gunshots', 'sounds of the victim', 'a loud, unknown sound, from the location of the murder']
    }
    
    # opening the case data save file to pull required information from
    with open('case data.json', 'r') as file:
        case_data = json.load(file)
    
    # all the pulled saved data from the case data, that is required to construct the witness data
    culprit_name = case_data['culprit name']
    suspects_list = case_data['selected suspects']
    is_witness_present = case_data['witness presence']
    witness_number = case_data['witness number']
    
    
    
    
    # generate the witnesses procedurally, just like the case data
    def generate_witnesses(is_witness_present, witness_number, witness_name, witness_mode_of_perception, event_witnessed, is_witness_suspect, save = True):
        # all the variables the function needs to function - the dictionary and other derived values
        witness_data = {
            'is witness present': is_witness_present,
            'witness number': witness_number,
            
            'witness names': witness_name,
            'mode of perception': witness_mode_of_perception,
            'event witnessed': event_witnessed,
            'is witness suspect': is_witness_suspect
        }
        
        if save:
            Save.save_witness_info(witness_data)
            
        return witness_data
    
    @staticmethod
    def generate_witnesses_file(witness_number, witness_name, witness_mode_of_perception, event_witnessed, is_witness_suspect, save = True):
        witness_description_list = []
        
        if int(witness_number) != 0:
            for witness in range(int(witness_number)):
                id = f'{witness + 1}'
                
                if is_witness_suspect[witness] == True:
                    witness_description = f'Witness {id} is {witness_name[witness]}, and they are also a suspect. They {witness_mode_of_perception[witness]} {event_witnessed[witness]}'
                    witness_description_list.append(witness_description)
                else:
                    witness_description = f'Witness {id} is {witness_name[witness]}. They {witness_mode_of_perception[witness]} {event_witnessed[witness]}'
                    witness_description_list.append(witness_description)
                    
                print(witness_description)
                
            if save:
                Save.save_witness_file(witness_description_list)
        else:
            witness_description = 'there are no witnesses to this case'
            
            if save:
                Save.save_witness_file(witness_description)
                
            print(witness_description)
        
    def read_witness_file():
        with open('witness file.json', 'r') as json_file:
            witness_file_data = json.load(json_file)
            
        return witness_file_data
    
    # the following functions retrive the required components for the final witness system to be formed
    def get_mode_of_perception(possible_modes_of_perception, witness_number):
        mode_of_perception_list = []
        
        if int(witness_number) != 0:
            for _ in range(int(witness_number)):
                mode_of_perception = random.choice(possible_modes_of_perception)
                mode_of_perception_list.append(mode_of_perception)
            
            return mode_of_perception_list
        else:
            return []
    
    def get_event_witnessed(mode_of_perception, possible_events_witnessed, witness_number):
        event_witnessed_list = []
        
        if int(witness_number) != 0:
            for i in range(int(witness_number)):
                if mode_of_perception[i] in possible_events_witnessed:
                    event_witnessed = random.choice(possible_events_witnessed[mode_of_perception[i]])
                    event_witnessed_list.append(event_witnessed)

            return event_witnessed_list
        else:
            return []
    
    def get_witness_names(culprit, culprit_name_list, witness_number):
        selected_witnesses = [None] * int(witness_number) # creates a list with indices that match the number of withnesses that is generated in case gen
        witnesses = culprit_name_list.copy() # creates a copy of the culprit list to act as the pool for the witnesses
        
        remaining_witnesses_list = list(filter(lambda item: item != culprit, witnesses)) # filters out the culprit from the pool for the witnesses, so that the culprit can never be assinged as a witness
        
        # checks if the selected witnesses list has indices of 0, as if it is zero, then this whole for loop will break, and the game breaks
        if int(witness_number) != 0:
            # loops through the entire selected witnesses list (which is empty until the following for loop runs), and adds random witnesses to the selected witnesses list - the witnesses are added from the remaining witnesses list
            for i in range(len(selected_witnesses)):
                selected_witnesses[i] = remaining_witnesses_list.pop(random.randrange(len(remaining_witnesses_list)))
                
            return selected_witnesses
        else:
            return []
            
    def get_is_witness_suspect(selected_suspects_list, selected_witness_list, witness_number):
        is_suspect_list = []
        
        if int(witness_number) != 0:
            for witness in selected_witness_list:
                if witness in selected_suspects_list:
                    is_suspect_list.append(True)
                else:
                    is_suspect_list.append(False)
            return is_suspect_list
        else:
            return []
    
    # calls all the methods that work together to show the detective info on the witnesses
    def generate_witness_and_witness_file_random():
        witness_data_save_file = 'witness data.json' # stores the path to the file that needs to save the witness data
        
        # sets each of the values returned from the helper methods as components into its own variables to be passed into the generate witnesses function as parameters
        selected_mode_of_perception = WitnessGen.get_mode_of_perception(WitnessGen.witness_mode_of_perception, WitnessGen.witness_number)
        selected_event_witnessed = WitnessGen.get_event_witnessed(selected_mode_of_perception, WitnessGen.event_witnessed_dict, WitnessGen.witness_number)
        selected_witness_names = WitnessGen.get_witness_names(WitnessGen.culprit_name, CaseGen.culprit_name_list, WitnessGen.witness_number)
        selected_is_witness_suspect = WitnessGen.get_is_witness_suspect(WitnessGen.suspects_list, selected_witness_names, WitnessGen.witness_number)
        
        # calls the functions required to generate the witness data and witness files
        WitnessGen.generate_witnesses(WitnessGen.is_witness_present, WitnessGen.witness_number, selected_witness_names, selected_mode_of_perception, selected_event_witnessed, selected_is_witness_suspect)
        
        with open(witness_data_save_file, 'r') as json_file:
            witness_data = json.load(json_file)
            
        # pulls the data required for the file to be generated from the witness data.json
        pulled_mode_of_perception = witness_data.get('mode of perception')
        pulled_event_witnessed = witness_data.get('event witnessed')
        pulled_witness_names = witness_data.get('witness names')
        pulled_is_witness_suspect = witness_data.get('is witness suspect')
        
        WitnessGen.generate_witnesses_file(WitnessGen.witness_number, pulled_witness_names, pulled_mode_of_perception, pulled_event_witnessed, pulled_is_witness_suspect)
        
        
WitnessGen.generate_witness_and_witness_file_random()