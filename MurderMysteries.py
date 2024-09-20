# murder mystery solve game
import random

class case_gen:
    culprit_name_list = ["Jerome", "Max", "Zach", "Tom", "Carl", "Tim", "Cooper", "Shaw", "Mat"] # holds the different possible names for the culprit
    victim_name_list = ['Sten', 'Troy', 'Dan'] # holds the different possible names for the victim
    murder_weapon_list = ['knife', 'gun', 'baseball bat', 'water'] # holds the different possible murder weapons
    murder_location_list = ['beach', 'park', 'house'] # holds the different possible murder locations
    weather_list = ['clear', 'rainy', 'foggy', 'windy'] # hold the different possible weather types
    time_of_day_list = ['dawn', 'morning', 'noon', 'afternoon', 'evening', 'dusk', 'night', 'midnight'] # holds the different possible time of day that the incident took place

    # dictionary to hold the different ways the victim can die with different weapons
    murder_type_dict = {
        "knife": ['stab', 'slit'],
        "gun": ['shot'],
        "baseball bat": ['smack'],
        "water": ['drown']
    }

    # dictionary to hold the different locations that can be injured through different murder types
    injury_location_dict = {
        "stab": ['stomach', 'chest', 'groin'],
        "slit": ['throat', 'left wrist', 'right wrist'],
        "shot": ['chest', 'forehead', 'stomach'],
        "smack": ['head', 'neck', 'chest'],
    }

    print("you have been transferred to the detective wing of the police department.")
    print("")

    # creates a detective profile
    def profile():
        name = input("what should the assoiates call you, detective?\n\n") # stores raw name input from user
        formatted_name = name.capitalize() # formats the name to capital letter first
        
        return "Detective " + formatted_name

    # generates a random case with random components passed into the case function. this is stored in a json file for comparison with the detective's criminal
    def generate_case(culprit_name, murder_weapon, murder_location, murder_type, weather, time_of_day, is_witness_present, witness_num, victim_name, has_injury, injury_location, suspects):
        # holds all the values that need to be save to the newly created, locked json file
        case_components = {
            'culprit name': culprit_name,
            'murder weapon': murder_weapon,
            'murder location': murder_location,
            'murder type': murder_type,
            'weather': weather,
            'time of day': time_of_day,
            'witness presence': is_witness_present,
            'witness number': witness_num,
            'victim name': victim_name,
            'has injury': has_injury,
            'injury location': injury_location,
            'selected suspects': suspects
        }
        
        print(case_components)
        return case_components
    
    # generates a case file from the same content of the case method. this is the story version that the detective sees
    def generate_case_file(victim_name, murder_weapon, has_injury, injury_location, murder_location, murder_type, weather, time_of_day, witness_num):
        if has_injury == True:
            case_file = f'{victim_name} was found dead in a {murder_location}. The cause of death\nwas a {murder_weapon} {murder_type} wound on the {injury_location}. It was\na {weather} {time_of_day}, and there is {witness_num} witnesses to this crime'
            print(case_file)
        else:
            case_file = f'{victim_name} was found dead in a {murder_location}. The cause of death\nwas {murder_type}ing. There were no injuries on the body according\nto autopsy reports. It was a {weather} {time_of_day} and\nthere is {witness_num} witnesses to this crime'
            print(case_file)

    # determines the name of the culprit
    def culprit_name(possible_culprit_names):
        culprit_name = random.choice(possible_culprit_names)
        
        return culprit_name

    # determines the name of the victim
    def victim_name(possible_victim_names):
        victim_name = random.choice(possible_victim_names)
        
        return victim_name

    # determines the location of the murder
    def murder_location(possible_murder_locations):
        murder_location = random.choice(possible_murder_locations)
        
        return murder_location

    # determines the weapon used for the murder
    def murder_weapon(possible_murder_weapons):
        murder_weapon = random.choice(possible_murder_weapons)
        
        return murder_weapon

    # determines how to murder was executed (were they stabbed? drowned? etc)
    def murder_type(weapon, possible_murder_types):
        if weapon in possible_murder_types:
            murder_type = random.choice(possible_murder_types[weapon])
            
        return murder_type

    # determines if the victim had an injury on the body in the crime scene
    def injury_location(murder_type, possible_injury_types):
        if murder_type in possible_injury_types:
            injury_location = random.choice(possible_injury_types[murder_type])
            
            return injury_location
        else:
            return None
        
    # bool function to determine if or if not the body has injuries
    def has_injuries(injury_location):
        if injury_location is not None:
            return True
        else:
            return False

    # determines the weather of the day of incident
    def weather(possible_weathers):
        weather = random.choice(possible_weathers)
        
        return weather

    # determines the time of the day
    def time_of_day(possible_times_of_day):
        time_of_day = random.choice(possible_times_of_day)
        
        return time_of_day

    # determines if there were witnesses present or not
    def is_witness_present():
        state_is_witness_present = random.choice([True, False])
        
        return state_is_witness_present

    # if yes, determines the number of witnesses
    def number_of_witnesses(is_witness_present):
        witness_present = is_witness_present
        
        if witness_present:
            number_of_witnesses = random.randint(1,3)
        else:
            number_of_witnesses = 0

        return str(number_of_witnesses), witness_present

    # returns a list of 4 suspects including 3 random suspects and the returned culprit himself
    def suspects(culprit, culprit_name_list):
        selected_suspects = [None] * 4 # creates an empty list of length 4 to be populated with the suspects of the case
        culprit_index_in_suspects_list = random.randint(0, 3) # generates a random number from within the length of the selected suspects to place the culprit in (the culprit name position is randomized so that the culprit name does not always show up at the same spot)
        suspects = culprit_name_list.copy() # creates a copy of the culprits name list to act as the suspect pool for the case
        
        selected_suspects.insert(culprit_index_in_suspects_list, culprit) # inserts the culprit name at the generated index value
        
        remaining_random_suspects = list(filter(lambda item: item != culprit, suspects)) # filters the remaining suspects after the culprit and picks 4 at random
        
        # loops through the entire selected suspects list to insert the random suspects in all the spots that do not match the randomly generated index value (where the culprit is present)
        for i in range(len(selected_suspects)):
            if i != culprit_index_in_suspects_list:
                selected_suspects[i] = remaining_random_suspects.pop(0)

        return selected_suspects

    # sets all the returned components of the case into their own variables so that the same instance of each function can be used across the different types (case and case file)
    selected_culprit_name = culprit_name(culprit_name_list)
    selected_murder_location = murder_location(murder_location_list)
    selected_weapon = murder_weapon(murder_weapon_list)
    selected_murder_type = murder_type(selected_weapon, murder_type_dict)
    selected_injury_location = injury_location(selected_murder_type, injury_location_dict)
    selected_time_of_day = time_of_day(time_of_day_list)
    selected_weather = weather(weather_list)
    selected_number_of_witness, selected_is_witness_present = number_of_witnesses(is_witness_present())
    selected_victim_name = victim_name(victim_name_list)
    selected_has_injuries = has_injuries(selected_injury_location)
    selected_suspects_list = suspects(selected_culprit_name, culprit_name_list)

    # testing for each of the separate components of the case

    # print(selected_culprit_name)
    # print(selected_murder_location)
    # print(selected_weapon)
    # print(selected_murder_type)
    # print(selected_injury_location)
    # print(selected_has_injuries)
    # print(selected_weather)
    # print(selected_time_of_day)
    # print(selected_is_witness_present)
    # print(selected_number_of_witness)
    # print(selected_suspects_list)
    

    generate_case(selected_culprit_name, selected_weapon, selected_murder_location, selected_murder_type, selected_weather, selected_time_of_day, selected_is_witness_present, selected_number_of_witness, selected_victim_name, selected_has_injuries, selected_injury_location, selected_suspects_list)
    # print("")
    # generate_case_file(selected_victim_name, selected_weapon, selected_has_injuries, selected_injury_location, selected_murder_location, selected_murder_type, selected_weather, selected_time_of_day, selected_number_of_witness)
