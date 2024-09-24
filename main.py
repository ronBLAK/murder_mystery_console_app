from case_gen import CaseGen
from detective_profile import DetectiveProfile
import detective_attributes
import json
import time

case_data_save_file = 'case data.json' # stores the file name that needs to be opened into a variable

# gets all the required methods from the case_gen class that are needed to generate a case
selected_culprit_name = CaseGen.get_culprit_name(CaseGen.culprit_name_list)
selected_murder_location = CaseGen.get_murder_location(CaseGen.murder_location_list)
selected_weapon = CaseGen.get_murder_weapon(CaseGen.murder_weapon_list)
selected_murder_type = CaseGen.get_murder_type(selected_weapon, CaseGen.murder_type_dict)
selected_injury_location = CaseGen.get_injury_location(selected_murder_type, CaseGen.injury_location_dict)
selected_time_of_day = CaseGen.get_time_of_day(CaseGen.time_of_day_list)
selected_weather = CaseGen.get_weather(CaseGen.weather_list)
selected_number_of_witness, selected_is_witness_present = CaseGen.get_number_of_witnesses(CaseGen.is_witness_present())
selected_victim_name = CaseGen.get_victim_name(CaseGen.victim_name_list)
selected_has_injuries = CaseGen.has_injuries(selected_injury_location)
selected_suspects_list = CaseGen.get_suspects(selected_culprit_name, CaseGen.culprit_name_list)

# gets and stores all information of detective from save file for detective and assigns it to variables to be used in main.py
fame = detective_attributes.fame
cases_solved = detective_attributes.cases_solved

# whether the user accpets or declines the case
def question_start_solve():
    print('enter 1 to accept case')
    print('enter 2 to decline and request new case')
    print('')
    start_solve = input('enter your choice here --> ')
    print('')
    
    return start_solve

print("you have been transferred to the detective wing of the police department.")
print("")

detective_name = DetectiveProfile.detective_name()
DetectiveProfile.get_detective_info_as_dict(detective_name, fame, cases_solved)
print('')

print(f'Hello {detective_name}, you have a case waiting for you.')
print('')

# calls all the functions that work to generate the case and case file
CaseGen.generate_case(selected_culprit_name, selected_weapon, selected_murder_location, selected_murder_type, selected_weather, selected_time_of_day, selected_is_witness_present, selected_number_of_witness, selected_victim_name, selected_has_injuries, selected_injury_location, selected_suspects_list)

# attempts to pull data from the case data save file and set it equal to new variables to be used to generate a case file for the generated case 
with open(case_data_save_file, 'r') as json_file:
    case_data = json.load(json_file)

pulled_culprit_name = case_data.get('culprit name')
pulled_murder_weapon = case_data.get('murder weapon')
pulled_murder_location = case_data.get('murder location')
pulled_murder_type = case_data.get('murder type')
pulled_weather = case_data.get('weather')
pulled_time_of_day = case_data.get('time of day')
pulled_witness_number = case_data.get('witness number')
pulled_victim_name = case_data.get('victim name')
pulled_has_injury = case_data.get('has injury')
pulled_injury_location = case_data.get('injury location')
pulled_suspects_list = case_data.get('selected suspects')
formatted_suspects_list = ', '.join(pulled_suspects_list)

CaseGen.generate_case_file(pulled_victim_name, pulled_murder_weapon, pulled_has_injury, pulled_injury_location, pulled_murder_location, pulled_murder_type, pulled_weather, pulled_time_of_day, pulled_witness_number, pulled_suspects_list, formatted_suspects_list)
print('')

# checks and validates the input, and shows a placeholder message for when the case solve implementation can be executed
while question_start_solve() != '1':
    print('New Case:')
    print('')
    selected_culprit_name = CaseGen.get_culprit_name(CaseGen.culprit_name_list)
    selected_murder_location = CaseGen.get_murder_location(CaseGen.murder_location_list)
    selected_weapon = CaseGen.get_murder_weapon(CaseGen.murder_weapon_list)
    selected_murder_type = CaseGen.get_murder_type(selected_weapon, CaseGen.murder_type_dict)
    selected_injury_location = CaseGen.get_injury_location(selected_murder_type, CaseGen.injury_location_dict)
    selected_time_of_day = CaseGen.get_time_of_day(CaseGen.time_of_day_list)
    selected_weather = CaseGen.get_weather(CaseGen.weather_list)
    selected_number_of_witness, selected_is_witness_present = CaseGen.get_number_of_witnesses(CaseGen.is_witness_present())
    selected_victim_name = CaseGen.get_victim_name(CaseGen.victim_name_list)
    selected_has_injuries = CaseGen.has_injuries(selected_injury_location)
    selected_suspects_list = CaseGen.get_suspects(selected_culprit_name, CaseGen.culprit_name_list)

    # calls all the functions that work to generate the case and case file
    CaseGen.generate_case(selected_culprit_name, selected_weapon, selected_murder_location, selected_murder_type, selected_weather, selected_time_of_day, selected_is_witness_present, selected_number_of_witness, selected_victim_name, selected_has_injuries, selected_injury_location, selected_suspects_list)

    # attempts to pull data from the case data save file and set it equal to new variables to be used to generate a case file for the generated case 
    with open(case_data_save_file, 'r') as json_file:
        case_data = json.load(json_file)

    pulled_culprit_name = case_data.get('culprit name')
    pulled_murder_weapon = case_data.get('murder weapon')
    pulled_murder_location = case_data.get('murder location')
    pulled_murder_type = case_data.get('murder type')
    pulled_weather = case_data.get('weather')
    pulled_time_of_day = case_data.get('time of day')
    pulled_witness_number = case_data.get('witness number')
    pulled_victim_name = case_data.get('victim name')
    pulled_has_injury = case_data.get('has injury')
    pulled_injury_location = case_data.get('injury location')
    pulled_suspects_list = case_data.get('selected suspects')
    formatted_suspects_list = ', '.join(pulled_suspects_list)

    CaseGen.generate_case_file(pulled_victim_name, pulled_murder_weapon, pulled_has_injury, pulled_injury_location, pulled_murder_location, pulled_murder_type, pulled_weather, pulled_time_of_day, pulled_witness_number, pulled_suspects_list, formatted_suspects_list)
    print('')

# this is what happens if the user selects a case instead of generating a new case
print('case selected')
print('opening investigator menu...')
print('')
time.sleep(3)

print('the case is all yours, detective...')
print('')
print('1. view detective profile')
print('2. open your notebook')
print('3. view case file')
print('4. open solve and submit menu')
print('5. search for clues at the crime scene')

# need to save detective info..
