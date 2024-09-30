import time
import os
from case_gen import CaseGen
from detective_profile import DetectiveProfile
from suspect_information import SuspectInformation
import detective_attributes

# gets and stores all information of detective from save file for detective and assigns it to variables to be used in main.py
fame = detective_attributes.fame
cases_solved = detective_attributes.cases_solved

# stores the names of different save files into variables
case_data_file_path = 'case data.json'
case_file_file_path = 'case file.json'
detective_data_file_path = 'detective data.json'
suspects_info_file_path = 'suspects info.json'

suspect_1_file_path = 'suspects 1 information file.json'
suspect_2_file_path = 'suspects 2 information file.json'
suspect_3_file_path = 'suspects 3 information file.json'
suspect_4_file_path = 'suspects 4 information file.json'
suspect_5_file_path = 'suspects 5 information file.json'

# whether the user accepts or declines the case
def question_start_solve():
    print('enter 1 to accept case')
    print('enter 2 to decline and request new case')
    print('')
    start_solve = input('enter your choice here --> ')
    print('')
    return start_solve

# function to display the commands that the user can choose
def commands():
    print('')
    print('1. view detective profile')
    print('2. open your notebook')
    print('3. view case file')
    print('4. search for clues at the crime scene')
    print('5. open solve and submit menu')
    print('6. view suspect information')
    print('7. exit')
    print('')

print("you have been transferred to the detective wing of the police department.")
print("")
print("--- enter any name other than the name of the previous detective's name to start a new account ---")

# asks the user for their detective name
detective_name = DetectiveProfile.detective_name()
print('')

# defines all actions available to detective in investigator menu, and their criteria
def user_menu_interaction(user_choice):
    if user_choice == '1':
        print('')
        print('Detective Profile:')
        print('')
        print(f'Detective Name: {detective_name}')
        print(f'Detective Fame: {fame}')
        print(f'Number of Cases Solved: {cases_solved}')
    elif user_choice == '2':
        print('you can open, read and edit your notebook in this menu')
    elif user_choice == '3':
        print('you can review the case file for the case in this menu')
    elif user_choice == '4':
        print('you can search for clues in the crime scene in this menu')
    elif user_choice == '5':
        print('you can submit who you think is the culprit, with the factual evidence in this menu')
    elif user_choice == '6':
        print('You can view all the suspects profiles here')
        SuspectInformation.generate_all_suspects_information()
    elif user_choice == '7':
        print('')
        print('--- Detective information and current case successfully saved---')
        print('--- Please remember the name of your detective account to revisit the case---')
    else:
        print('invalid input. please try again..')
        
def user_menu_interaction_with_read(user_choice):
    if user_choice == '1':
        print('')
        print('Detective Profile:')
        print('')
        print(f'Detective Name: {detective_name}')
        print(f'Detective Fame: {fame}')
        print(f'Number of Cases Solved: {cases_solved}')
    elif user_choice == '2':
        print('you can open, read and edit your notebook in this menu')
    elif user_choice == '3':
        print('you can review the case file for the case in this menu')
    elif user_choice == '4':
        print('you can search for clues in the crime scene in this menu')
    elif user_choice == '5':
        print('you can submit who you think is the culprit, with the factual evidence in this menu')
    elif user_choice == '6':
        print('You can view all the suspects profiles here')
        print(SuspectInformation.read_suspect_1_report())
        print('')
        print(SuspectInformation.read_suspect_2_report())
        print('')
        print(SuspectInformation.read_suspect_3_report())
        print('')
        print(SuspectInformation.read_suspect_4_report())
        print('')
        print(SuspectInformation.read_suspect_5_report())
    elif user_choice == '7':
        print('')
        print('--- Detective information and current case successfully saved---')
        print('--- Please remember the name of your detective account to revisit the case---')
    else:
        print('invalid input. please try again..')

# The main flow of the game based on whether the save files exist
if os.path.exists(case_file_file_path) and os.path.exists(case_data_file_path) and os.path.exists(detective_data_file_path) and os.path.exists(suspects_info_file_path) and os.path.exists(suspect_1_file_path) and os.path.exists(suspect_2_file_path) and os.path.exists(suspect_3_file_path) and os.path.exists(suspect_4_file_path) and os.path.exists(suspect_5_file_path):
    if detective_name == DetectiveProfile.read_detective_info():
        print(f'Hello {detective_name}. Let\'s pick up your case right where you left it off.')
        print('')
        print(CaseGen.read_case_file())
        print('')
        print('Opening investigator menu...')
        print('')
        time.sleep(1)

        print('The case is all yours, detective...')
        commands()
        print('')

        while True:
            user_menu_choice = input('Enter your choice here --> ')
            if user_menu_choice == '7':
                user_menu_interaction_with_read(user_menu_choice)
                break
            else:
                user_menu_interaction_with_read(user_menu_choice)
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
        while question_start_solve() != '1':
            print('New Case:')
            CaseGen.generate_case_and_case_file_random()

        # This is what happens if the user selects the given case instead of generating a new case
        print('Case selected')
        print('Opening investigator menu...')
        print('')
        time.sleep(1)

        print('The case is all yours, detective...')
        commands()
        print('')

        while True:
            user_menu_choice = input('Enter your choice here --> ')
            if user_menu_choice == '7':
                user_menu_interaction(user_menu_choice)
                break
            else:
                user_menu_interaction(user_menu_choice)
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
    while question_start_solve() != '1':
        print('New Case:')
        CaseGen.generate_case_and_case_file_random()

    # This is what happens if the user selects the given case instead of generating a new case
    print('Case selected')
    print('Opening investigator menu...')
    print('')
    time.sleep(1)

    print('The case is all yours, detective...')
    commands()
    print('')

    while True:
        user_menu_choice = input('Enter your choice here --> ')
        if user_menu_choice == '7':
            user_menu_interaction(user_menu_choice)
            break
        else:
            user_menu_interaction(user_menu_choice)
            print('')
