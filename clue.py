import random
import json
from save import Save
from enum import Enum, auto

# this class stores the different kinds of clues that can be left behind to aid the detective in the solving of the case
class ClueTypesStates(Enum):
    # main headers - for the type of clue found
    BIOLOGICAL_EVIDENCE = 'biological evidence'
    NOTES = 'notes' # the clue that this state generates is not random, and hence is generated differently to the other clues
    CARELESS_MISTAKES = 'careless mistakes'
    
class ClueStates(Enum):
    # the types of clues that can be left behind by the killer - types of careless mistakes
    MURDER_WEAPON = 'murder weapon' # this is also not randomly generated (the presence of this clue IS random, but not the actual clue). it is the murder weapon that is generted in the case class
    FINGERPRINTS = 'fingerprints'
    FOOTPRINTS = 'footprints'

class Clue:
    clue_types = [
        ClueTypesStates.BIOLOGICAL_EVIDENCE,
        ClueTypesStates.NOTES,
        ClueTypesStates.CARELESS_MISTAKES
    ]
    clues_dict = {
        'biological evidence': ['hair', 'blood'], # need to make it so that the options for blood and hair are available only if there is a wound by the knife or the gun - otherwise, only hair can be found for now
        'careless mistakes': [
            ClueStates.MURDER_WEAPON.value,
            ClueStates.FINGERPRINTS.value,
            ClueStates.FOOTPRINTS.value
        ]
    }
    
    def generate_clue_data(clue_type_number, clue_types, visibility_status, clue_number, clues):
        clue_data = {
            'number of clues': clue_type_number,
            'selected clue types': clue_types,
            'clue visibility status': visibility_status,
        }
        
    # the functions below generate information regarding the clue types
    
    # this function generates the number of clue types that are present (selects from Clue.clue_types)
    def get_clue_type_number(clue_type_list):
        clue_types_num = random.randint(1, len(clue_type_list))
        
        return clue_types_num
    
    def get_clue_types(clue_types_number, clue_types_list):
        clue_types_list_copy = clue_types_list.copy()
        selected_clue_types = []
        
        for i in range(clue_types_number):
            random_clue_type = random.choice(clue_types_list_copy)
            selected_clue_types.append(random_clue_type)
            clue_types_list_copy.remove(random_clue_type)
            
        return selected_clue_types
    
    def get_clue_type_visiblity_status(selected_clue_types_list):
        visibility_status = []
        
        for clue in selected_clue_types_list:
            visibility_status.append(random.choice([True, False]))
        
        return visibility_status
    
    # the functions below generate information regarding the sub-clue types
    
    # i am not creating a separate function for the clue number, as the clues for each types vary - some clue types have 2 clues that they could generate and some have three. so im going to use the inbuilt random.randint function, passing the desired values each time, which grants me flexibility on the range of number the code should expect
    
    def get_clues(biological_evidence_number, careless_mistake_number, clue_types_list, clues_dict):
        clues_dict_copy = clues_dict.copy()
        clues = [] # this is the list that appends all the below clue lists into one grandfather list
                
        for clue_type in clue_types_list:
            if clue_type == ClueTypesStates.BIOLOGICAL_EVIDENCE:
                for biological_evidence in range(biological_evidence_number):
                    random_bio_evidence = random.choice(clues_dict_copy[ClueTypesStates.BIOLOGICAL_EVIDENCE.value])
                    biological_evidence = random_bio_evidence
                    clues.append(biological_evidence)
                    clues_dict_copy[ClueTypesStates.BIOLOGICAL_EVIDENCE.value].remove(random_bio_evidence)
            elif clue_type == ClueTypesStates.CARELESS_MISTAKES:
                for careless_mistake in range(careless_mistake_number):
                    random_careless_mistake = random.choice(clues_dict_copy[ClueTypesStates.CARELESS_MISTAKES.value])
                    careless_mistake = random_careless_mistake
                    clues.append(careless_mistake)
                    clues_dict_copy[ClueTypesStates.CARELESS_MISTAKES.value].remove(random_careless_mistake)
            elif clue_type == ClueTypesStates.NOTES:
                note = 'note' # this just returns a string because notes do not have sub lists that they can pick a component from, like the careless mistakes or bio evidence. they will have just one value, which will be returned by another function just for the notes - so as of now, it is just a placeholder in the clues list
                clues.append(note)
            
        return clues
                
    

selected_clue_types_number = Clue.get_clue_type_number(Clue.clue_types)
print(Clue.clue_types)
selected_clue_types = Clue.get_clue_types(selected_clue_types_number, Clue.clue_types)
print(Clue.clue_types)
selected_clue_type_visibility_status = Clue.get_clue_type_visiblity_status(selected_clue_types)
selected_biological_evidence_num = random.randint(1, 2)
selected_careless_mistakes_num = random.randint(1, 3)
selected_clues = Clue.get_clues(selected_biological_evidence_num, selected_careless_mistakes_num, selected_clue_types, Clue.clues_dict)

print(selected_clue_types)
print(selected_clues)