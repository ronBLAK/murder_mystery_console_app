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
    print('')
    
def user_menu_selection():
    user_selection = input('enter your choice here: ')
    return user_selection

print("you have been transferred to the detective wing of the police department.")
print("")

# asks the user for their detective name
detective_name = DetectiveProfile.detective_name()
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

