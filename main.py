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
        enter_letter = input(Fore.GREEN + "Select a Letter from the Above Box menu : ")

        if enter_letter.isalpha():
            if enter_letter in ["a", "b", "c", "d"]:
                while True:
                    break
            else:
                Interface.onboarding(ErrorMessage=True)
        else:
            Interface.onboarding(ErrorMessage=True)
            print("\nInput must be a above mentioned letter\n")
        if enter_letter == "c":
            print(Fore.LIGHTWHITE_EX + Fore.LIGHTWHITE_EX)
            DataCheck.basic_data_check(boarding_state=enter_letter)

    def boarded():
        user_weight = float(DataFetcher.get_key_val(key="user_weight"))
        user_goal = int(DataFetcher.get_key_val(key="user_goal"))
        weight_loss = Calculations.weight_loss_calc()
        aprx_new_weight = user_weight - weight_loss
        print("|" * 26 + "welcome" + "|" * 42)
        print("||||Goal||||Time Passed||||Approximate Weight Loss||Approximate New Weight")
        print("---------------------------------------------------------------------------")
        print(f"||{Fore.BLUE}{user_goal}-days{Fore.LIGHTWHITE_EX}||||{Fore.BLUE} 00-hours {Fore.LIGHTWHITE_EX}"
              f"|||||||||||| {Fore.BLUE}{weight_loss}-kg{Fore.LIGHTWHITE_EX} |||||||||||||||{Fore.BLUE}"
              f" {aprx_new_weight}-kg ||||{Fore.LIGHTWHITE_EX}")


class DataFetcher:
    stage1 =False
    def get_key_val(key, ):
        with open('data.json') as json_file:
            data = json.load(json_file)
            for k, v in data.items():
                if k == key:
                    return v
            else:
                Interface.onboarding()




class Calculations:
    user_weight = float(DataFetcher.get_key_val(key="user_weight"))
    user_goal = int(DataFetcher.get_key_val(key="user_goal"))

    wfc_multiplication = [0.85, 1.90, 2.72, 3.41, 4.02, 4.58, 5.09, 5.57, 6.02, 6.45, 6.85, 7.24,
                          7.62, 7.98, 8.33]

    def weight_loss_calc(form_wfc=wfc_multiplication, user_weight=user_weight, user_goal=user_goal):
        if user_goal < 16:
            weight_loss = (user_weight / 100 * float(form_wfc[user_goal - 1]))
        else:
            multiplier_past_15 = 8.33 + ((user_goal - 15) * 0.32)
            weight_loss = (user_weight / 100 * float(multiplier_past_15))
        return weight_loss



""" <<<Onboarding data processer>>>
    used in case user chooses to skip the signup process.
    but in case of signup also is used to collect minimal needed data for calculations.
"""


class BasicData:
    # USED FOR CHECKING IF SOME VARIABLE IS WITHIN LIST
    def str_check(option1=None, option2=None, option3=None, option4=None, unit=None):
        user_input = input("input " + unit + " : ")
        user_input_lower = user_input.lower()
        if user_input_lower:
            while True:
                if user_input_lower in [str(option1), option2, option3, option4]:
                    print(user_input)
                    return str(user_input_lower)
                else:
                    print(Fore.RED + "\nPlease input valid " + unit + "\n" + ("*") * 60)
                    BasicData.str_check(unit=unit, option1=option1, option2=option2, option3=option3,
                                        option4=option4)
                    break
        else:
            print(Fore.RED + "\nfield can't be empty\n" + ("*") * 60)
            BasicData.str_check(unit=unit, option1=option1, option2=option2, option3=option3,
                                option4=option4)

    # USED FOR CHECKING IF SOME VARIABLE IS WITHING RANGE
    def range_check(num_var, range_s, range_e, message):
        if num_var.isnumeric():
            while True:
                if int(num_var) in range(range_s, range_e):
                    return num_var
                else:
                    return (Fore.RED + "\nPlease input valid " + message + "\n" + ("*") * 60)
        else:
            return (Fore.RED + "\nInput must be a number\n" + ("*") * 60)

    def check(unit_name, range_min, range_max, suffix=None):
        # User input field
        user_input = input(Fore.LIGHTWHITE_EX + "input " + unit_name + " " + suffix + " : ")
        user_unit = (
            BasicData.range_check(num_var=user_input, range_s=range_min, range_e=range_max, message=unit_name))
        # Loops until number is within range
        while user_unit != user_input:
            print(user_unit)
            user_input = input(Fore.LIGHTWHITE_EX + "input " + unit_name + " " + suffix + " : ")
            user_unit = (BasicData.range_check(num_var=user_input, range_s=range_min, range_e=range_max,
                                               message=unit_name))

        # returns user input
        else:
            return user_unit


# TODO
class Account():
    pass


"""check if local data exist"""



###SKIP###
class DataCheck():
    def where_json(file_name):
        return os.path.exists(file_name)

    def basic_data_check(boarding_state):
        if DataCheck.where_json('data.json'):
            if boarding_state == "c":
                Interface.boarded()
            pass

        else:

            """Create local data dict"""
            data = {
                'user_gender': BasicData.str_check(unit="gender", option1="male", option2="female", option3="1",
                                                   option4="2"),
                'user_weight': BasicData.check(unit_name="weight", range_min=50, range_max=200, suffix="in kg"),
                'user_height': BasicData.check(unit_name="height", range_min=100, range_max=250, suffix="in cm"),
                'user_goal': BasicData.check(unit_name="goal", range_min=1, range_max=30, suffix="in days")
            }

            """Create and save data to data.json"""

            with open('data.json', 'w') as outfile:
                json.dump(data, outfile)

            if boarding_state == "c":
                Interface.boarded()




def main():
    Interface.onboarding()


if __name__ == '__main__':
    main()
