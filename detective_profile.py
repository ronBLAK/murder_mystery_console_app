from save_case import Save

class DetectiveProfile:
    # creates a detective profile
    @staticmethod
    def detective_name():
        name = input("what should the assoiates call you, detective?\n\n") # stores raw name input from user
        formatted_name = name.capitalize() # formats the name to capital letter first
        
        return "Detective " + formatted_name
    
    def get_detective_info_as_dict(detective_name):
        detective_info = {
            'detective name': detective_name
        }
        
        return detective_info
        # need to add more variables that define the detective as the parameters for this function..