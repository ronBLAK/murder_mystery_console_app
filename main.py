from case_gen import CaseGen
from detective_profile import DetectiveProfile
import detective_attributes
import time

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

# function to display the commands that the user can choose
def commands():
    print('')
    print('1. view detective profile')
    print('2. open your notebook')
    print('3. view case file')
    print('4. search for clues at the crime scene')
    print('5. open solve and submit menu')
    print('6. exit')
    print('')

# function to store criteria for each action that the detective can carry out while attempting to solve the case
def user_menu_interaction(user_choice):
    if user_choice == '1':
        print('you can view the profile of your existing detective account in this menu')
    elif user_choice == '2':
        print('you can open, read and edit your notebook in this menu')
    elif user_choice == '3':
        print('you can review the case file for the case in this menu')
    elif user_choice == '4':
        print('you can search for clues in the crime scene in this menu')
    elif user_choice == '5':
        print('you can submit who you think is the culprit, with the factual evidence in this menu')
    elif user_choice == '6':
        print('exiting...')
    else:
        print('invalid input. please try again..')

print("you have been transferred to the detective wing of the police department.")
print("")

# asks the user for their detective name
detective_name = DetectiveProfile.detective_name()

# checks if the detective name entered is already present in the dictionary
# if name present in dictionary, does not call the save function, and shows the previously saved name in dictionary. also displays previously saved case, as this is should be the case that is affiliated with the previous detective
if detective_name == DetectiveProfile.read_detective_info():
    print(f'Hello {detective_name}. Lets pick up your case right where you left it off')
    DetectiveProfile.get_detective_info_as_dict(detective_name, fame, cases_solved,save = False)
    print('')
    print(CaseGen.read_case_file())
    print('')
    print('opening investigator menu...')
    print('')
    time.sleep(1)

    print('the case is all yours, detective...')
    commands()
    print('')

    while True:
        user_menu_choice = input('enter your choice here --> ')

        if user_menu_choice == '6':
            user_menu_interaction(user_menu_choice)
            break
        else:
            user_menu_interaction(user_menu_choice)
            print('')
# if not present in dictionary, proceeds to save the new detective info into dictionary, and generates a new case
else:
    DetectiveProfile.get_detective_info_as_dict(detective_name, fame, cases_solved)
    print('')

    print(f'Hello {detective_name}, you have a case waiting for you.')
    print('')

    # generates random case, and random case file according to information from the case
    CaseGen.generate_case_and_case_file_random()

    # checks and validates the input
    while question_start_solve() != '1':
        print('New Case:')
        CaseGen.generate_case_and_case_file_random()

    # this is what happens if the user selects the given case instead of generating a new case
    print('case selected')
    print('opening investigator menu...')
    print('')
    time.sleep(1)

    print('the case is all yours, detective...')
    commands()
    print('')

    while True:
        user_menu_choice = input('enter your choice here --> ')

        if user_menu_choice == '6':
            user_menu_interaction(user_menu_choice)
            break
        else:
            user_menu_interaction(user_menu_choice)
            print('')
