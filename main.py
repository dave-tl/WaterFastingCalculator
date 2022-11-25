import json
import os
import time
from colorama import Fore, Back, Style



class Interface:


    def onboarding(ErrorMessage=False):
        print(("*") * 60)
        print("========== WELCOME TO WATER FAST CALCULATOR ==========")
        print(("*") * 60)
        print("========== (a). Sign In ============")
        print("========== (b). Sign Up ============")
        print("========== (c). Skip ============\n")
        print("========== (d). Quit ============")
        print(("*") * 60)
        if ErrorMessage is True:
            print(Fore.RED + "Input must be a above mentioned letter\n" + ("*") * 60)
        EnterLetter = input(Fore.GREEN + "Select a Letter from the Above Box menu : ")

        if EnterLetter.isalpha():
            if EnterLetter in ["a", "b", "c", "d"]:
                while True:
                    break
            else:
                Interface.onboarding(ErrorMessage=True)
        else:
            Interface.onboarding(ErrorMessage=True)
            print("\nInput must be a above mentioned letter\n")
        if EnterLetter == "c":
            basic_data_check()




""" <<<Onboarding>>>
    used in case user chooses to skip the signup process.
    but in case of signup also is used to collect minimal needed data for calculations.
"""


class InputValidation:
    # USED FOR CHECKING IF SOME VARIABLE IS WITHIN LIST

    def str_check(option1=None, option2=None, option3=None, option4=None, unit=None):
        user_input = input(Fore.LIGHTWHITE_EX+"input " + unit + " : "+Fore.RESET)
        user_input_lower = user_input.lower()
        if user_input_lower:
            while True:
                if user_input_lower in [str(option1), option2, option3, option4]:
                    return str(user_input_lower)
                else:
                    print(Fore.RED + "\nPlease input valid " + unit + "\n" + ("*") * 60+Fore.RESET)
                    InputValidation.str_check(unit=unit, option1=option1, option2=option2, option3=option3,
                                        option4=option4)
                    break
        else:
            print(Fore.RED + "\nfield can't be empty\n" + ("*") * 60+Fore.RESET)
            InputValidation.str_check(unit=unit, option1=option1, option2=option2, option3=option3,
                                option4=option4)
    def r_check(num_var, range_s, range_e, message):
        if num_var.isnumeric():
            while True:
                if int(num_var) in range(range_s, range_e):
                    return num_var
                else:
                    return (Fore.RED + "\nPlease input valid " + message + "\n" + ("*") * 60+Fore.RESET)
        else:
            return (Fore.RED + "\nInput must be a number\n" + ("*") * 60+Fore.RESET)

    def range_check(unit_name, range_min, range_max, suffix=None):
        # User input field
        user_input = input(Fore.LIGHTWHITE_EX + "input " + unit_name + " " + suffix + " : "+Fore.RESET)
        user_unit = (
            InputValidation.r_check(num_var=user_input, range_s=range_min, range_e=range_max, message=unit_name))
        # Loops until number is within range
        while user_unit != user_input:
            print(user_unit)
            user_input = input(Fore.LIGHTWHITE_EX + "input " + unit_name + " " + suffix + " : "+Fore.RESET)
            user_unit = (InputValidation.r_check(num_var=user_input, range_s=range_min, range_e=range_max,
                                                 message=unit_name))

        # returns user input
        else:
            return user_unit


"""check if local data exist"""


###SKIP###
def basic_data_check():
    if where_json('data.json'):
        pass

    else:
        print(Fore.LIGHTWHITE_EX + "\nBasic data is required for calculations\n" + Fore.RESET)
        """Create local data dict"""
        data = {
            'user_gender': InputValidation.str_check(unit="gender", option1="male", option2="female", option3="1",
                                                   option4="2"),
            'user_weight': InputValidation.range_check(unit_name="weight", range_min=50, range_max=200, suffix="in kg"),
            'user_height': InputValidation.range_check(unit_name="height", range_min=100, range_max=250, suffix="in cm"),
            'user_goal': InputValidation.range_check(unit_name="goal", range_min=1, range_max=30, suffix="in days")
        }

        """Create and save data to data.json"""

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)



def where_json(file_name):
    return os.path.exists(file_name)


def main():
    Interface.onboarding()


if __name__ == '__main__':
    main()
