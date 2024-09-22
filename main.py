from case_gen import CaseGen

print("you have been transferred to the detective wing of the police department.")
print("")
name = input("what should the assoiates call you, detective?\n\n") # stores raw name input from user
formatted_name = name.capitalize() # formats the name to capital letter first

print(f'Hello Detective {formatted_name}, you have a case waiting for you.')
print('')

# calls all the functions that work to generate the case and case file
CaseGen.generate_case(CaseGen.selected_culprit_name, CaseGen.selected_weapon, CaseGen.selected_murder_location, CaseGen.selected_murder_type, CaseGen.selected_weather, CaseGen.selected_time_of_day, CaseGen.selected_is_witness_present, CaseGen.selected_number_of_witness, CaseGen.selected_victim_name, CaseGen.selected_has_injuries, CaseGen.selected_injury_location, CaseGen.selected_suspects_list)
CaseGen.generate_case_file(CaseGen.selected_victim_name, CaseGen.selected_weapon, CaseGen.selected_has_injuries, CaseGen.selected_injury_location, CaseGen.selected_murder_location, CaseGen.selected_murder_type, CaseGen.selected_weather, CaseGen.selected_time_of_day, CaseGen.selected_number_of_witness, CaseGen.selected_suspects_list, CaseGen.formatted_selected_suspects_list)

print('')

def question_start_solve():
    start_solve = input('press 1 to start solving this case: ')
    
    if start_solve == '1':
        print('the case solving process begins here.')
    while start_solve() != '1':
        question_start_solve()