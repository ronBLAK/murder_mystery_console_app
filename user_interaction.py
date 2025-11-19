import time
from case_gen import CaseGen
from suspects_info import SuspectsInfo
from witness_gen import WitnessGen
from detective_profile import DetectiveProfile
from detective_attributes import DetectiveAttributes

class UserInteraction:
    # whether the user accepts or declines the case
    def question_start_solve():
        print('')
        print('enter 1 to accept case')
        print('enter 2 to decline and request new case')
        print('')
        start_solve = input('enter your choice here --> ')
        print('')
        return start_solve
    
    # function to display the commands that the user can choose
    def commands():
        print('')
        print('1. exit')
        print('2. view detective profile')
        print('3. open your notebook')
        print('4. view case file')
        print('5. search for clues at the crime scene')
        print('6. open solve and submit menu')
        print('7. view suspect information')
        print('8. view witness list for crime')
        print('')
        
    # defines all actions available to detective in investigator menu, and their criteria - this version handles user input when the data is being generated - i.e. for the first time a case is loaded - this is the function that loads the values for the case
    def user_menu_interaction(user_choice):
        if user_choice == '1': # exit
            print('')
            print('--- Detective information and current case successfully saved---')
            print('--- Please remember the name of your detective account to revisit the case---')
        elif user_choice == '2': # view detective profile
            print('')
            print('Detective Profile:')
            print('')
            print(f'Detective Name: {DetectiveProfile.detective_name}')
            print(f'Detective Fame: {DetectiveAttributes.fame}')
            print(f'Number of Cases Solved: {DetectiveAttributes.cases_solved}')
            print('')
            time.sleep(2)
            UserInteraction.commands()
        elif user_choice == '3': # open notebook
            print('this feature is still in development - please use a pen and paper')
            print('')
            time.sleep(2)
            UserInteraction.commands()
        elif user_choice == '4': # view case file
            print('you can review the case file for the case in this menu')
            print('')
            print('')
            print(CaseGen.read_case_file())
            print('')
            time.sleep(2)
            UserInteraction.commands()
        elif user_choice == '5': # clue search
            print('you can search for clues in the crime scene in this menu')
            print('')
            time.sleep(2)
            UserInteraction.commands()
        elif user_choice == '6': # solve and submit
            print('you can submit who you think is the culprit, with the factual evidence in this menu')
            print('')
            time.sleep(2)
            UserInteraction.commands()
        elif user_choice == '7': # view suspect information
            print('You can view all the suspects profiles here')
            print('')
            print('')
            SuspectsInfo.generate_suspects_report_random()
            print('')
            time.sleep(2)
            UserInteraction.commands()
        elif user_choice == '8':
            print('You can view information about all the witnesses here')
            print('')
            print('')
            WitnessGen.generate_witness_and_witness_file_random()
            print('')
            time.sleep(2)
            UserInteraction.commands()
        else:
            print('invalid input. please try again..')
            print('')
            time.sleep(2)
            UserInteraction.commands()
    
    # defines all possible user interaction with the interface - this version of the function handles when the generated info has to be read from an existing save file - this function is the one that is called for after the same file is ready
    def user_menu_interaction_with_read(user_choice):
        if user_choice == '1': # exit
            print('')
            print('--- Detective information and current case successfully saved---')
            print('--- Please remember the name of your detective account to revisit the case---')
        elif user_choice == '2': # view detective profile
            print('')
            print('Detective Profile:')
            print('')
            print(f'Detective Name: {DetectiveProfile.detective_name}')
            print(f'Detective Fame: {DetectiveAttributes.fame}')
            print(f'Number of Cases Solved: {DetectiveAttributes.cases_solved}')
            print('')
            time.sleep(2)
            UserInteraction.commands()
        elif user_choice == '3': # open notebook
            print('this feature is still in development - please use a pen and paper')
            print('')
            time.sleep(2)
            UserInteraction.commands()
        elif user_choice == '4': # view case file
            print('you can review the case file for the case in this menu')
            print('')
            print('')
            print(CaseGen.read_case_file())
            print('')
            time.sleep(2)
            UserInteraction.commands()
        elif user_choice == '5': # clue search
            print('you can search for clues in the crime scene in this menu')
            print('')
            time.sleep(2)
            UserInteraction.commands()
        elif user_choice == '6': # solve and submit
            print('you can submit who you think is the culprit, with the factual evidence in this menu')
            print('')
            time.sleep(2)
            UserInteraction.commands()
        elif user_choice == '7': # view suspect information
            print('You can view all the suspects profiles here')
            print('')
            print('')
            print(SuspectsInfo.read_suspect_report())
            print('')
            time.sleep(2)
            UserInteraction.commands()
        elif user_choice == '8':
            print('You can view information about all the witnesses here')
            print('')
            print('')
            WitnessGen.read_witness_file()
            print('')
            time.sleep(2)
            UserInteraction.commands()
        else:
            print('invalid input. please try again..')
            print('')
            time.sleep(2)
            UserInteraction.commands()