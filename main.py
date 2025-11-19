import time
import os
from user_interaction import UserInteraction
from case_gen import CaseGen
from detective_profile import DetectiveProfile
from detective_attributes import DetectiveAttributes
#import notebook

# gets and stores all information of detective from save file for detective and assigns it to variables to be used in main.py
fame = DetectiveAttributes.fame
cases_solved = DetectiveAttributes.cases_solved

# stores the names of different save files into variables
case_data_file_path = 'case data.json'
case_file_file_path = 'case file.json'
detective_data_file_path = 'detective data.json'
suspects_info_file_path = 'suspects info.json'
suspect_report_file_path = 'suspects file.json'
witness_data_file_path = 'witness data.json'
witness_report_file_path = 'witness file.json'

suspect_generated = False

print("you have been transferred to the detective wing of the police department.")
print("")
print("--- enter any name other than the name of the previous detective's name to start a new account ---")

# asks the user for their detective name
detective_name = DetectiveProfile.detective_name()
print('')

# The main flow of the game based on whether the save files exist
if os.path.exists(case_file_file_path) and os.path.exists(case_data_file_path) and os.path.exists(detective_data_file_path) and os.path.exists(suspects_info_file_path) and os.path.exists(suspect_report_file_path) and os.path.exists(witness_data_file_path) and os.path.exists(witness_report_file_path):
    if detective_name == DetectiveProfile.read_detective_info():
        print(f'Hello {detective_name}. Let\'s pick up your case right where you left it off.')
        print('')
        print(CaseGen.read_case_file())
        print('')
        print('Opening investigator menu...')
        print('')
        time.sleep(1)

        print('The case is all yours, detective...')
        time.sleep(2)
        UserInteraction.commands()
        print('')

        while True:
            print('')
            user_menu_choice = input('Enter your choice here --> ')
            print('')
            if user_menu_choice == '1':
                UserInteraction.user_menu_interaction_with_read(user_menu_choice)
                break
            else:
                UserInteraction.user_menu_interaction_with_read(user_menu_choice)
                print('')
    else:
        fame = 0
        cases_solved = 0

        DetectiveProfile.get_detective_info_as_dict(detective_name, fame, cases_solved)
        print('')

        print(f'Hello {detective_name}. I am Trevor, your in-charge. You seem new to this\nfield. Let\'s see what you\'ve got. You have a new case waiting for you.')
        print('')

        # Generates random case, and random case file according to information from the case
        CaseGen.generate_case_and_case_file_random()

        # Checks and validates the input
        while UserInteraction.question_start_solve() != '1':
            print('New Case:')
            CaseGen.generate_case_and_case_file_random()

        # This is what happens if the user selects the given case instead of generating a new case
        print('Case selected')
        print('Opening investigator menu...')
        print('')
        time.sleep(1)

        print('The case is all yours, detective...')
        time.sleep(2)
        UserInteraction.commands()
        print('')

        while True:
            print('')
            user_menu_choice = input('Enter your choice here --> ')
            print('')
            if user_menu_choice == '1':
                UserInteraction.user_menu_interaction(user_menu_choice)
                break
            else:
                UserInteraction.user_menu_interaction(user_menu_choice)
                print('')
else:
    fame = 0
    cases_solved = 0

    DetectiveProfile.get_detective_info_as_dict(detective_name, fame, cases_solved)
    print('')

    print(f'Hello {detective_name}. I am Trevor, your in-charge. You seem new to this\nfield. Let\'s see what you\'ve got. You have a new case waiting for you.')
    print('')

    # Generates random case, and random case file according to information from the case
    CaseGen.generate_case_and_case_file_random()

    # Checks and validates the input
    while UserInteraction.question_start_solve() != '1':
        print('New Case:')
        CaseGen.generate_case_and_case_file_random()

    # This is what happens if the user selects the given case instead of generating a new case
    print('Case selected')
    print('Opening investigator menu...')
    print('')
    time.sleep(1)

    print('The case is all yours, detective...')
    time.sleep(2)
    UserInteraction.commands()
    print('')

    while True:
        print('')
        user_menu_choice = input('Enter your choice here --> ')
        print('')
        if user_menu_choice == '1':
            UserInteraction.user_menu_interaction(user_menu_choice)
            break
        else:
            UserInteraction.user_menu_interaction(user_menu_choice)
            print('')