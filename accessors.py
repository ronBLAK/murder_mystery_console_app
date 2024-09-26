from case_gen import CaseGen

def access_culprit_name(self):
    culprit_name = CaseGen().generate_case_and_case_file_random()
    return culprit_name