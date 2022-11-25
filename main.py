import json
import os

print("************************************************************")
print("========== WELCOME TO WATER FAST CALCULATOR ==========")
print("************************************************************")
print("========== (a). Sign In ============")
print("========== (b). Sign Up ============")
print("========== (c). Skip ============\n")
print("========== (d). Quit ============")
print("************************************************************")

EnterLetter = input("Select a Letter from the Above Box menu : ")


class BasicData:

    def range_check(num_var, range_s, range_e, message):
        if num_var.isnumeric():
            while True:
                if int(num_var) in range(range_s, range_e):
                    return num_var
                else:
                    return ("\nPlease input valid " + message + "\n")
        else:
            return ("\nInput must be a number\n")

    def check(unit_name, range_min, range_max):
        """User input field"""
        user_input = input("input " + unit_name + " : ")
        user_unit = (
            BasicData.range_check(num_var=user_input, range_s=range_min, range_e=range_max, message=unit_name))
        while user_unit != user_input:
            print(user_unit)
            user_input = input("input " + unit_name + " : ")
            user_unit = (BasicData.range_check(num_var=user_input, range_s=range_min, range_e=range_max,
                                               message=unit_name))

        else:
            return user_unit


"""check if local data exist"""


def where_json(file_name):
    return os.path.exists(file_name)


if where_json('data.json'):
    pass

else:

    """Create local data dict"""
    data = {
        'user_weight': BasicData.check(unit_name="weight", range_min=50, range_max=200),
        'user_height': BasicData.check(unit_name="height", range_min=100, range_max=250),
        'user_goal': BasicData.check(unit_name="goal", range_min=1, range_max=30)
    }

    """Save the data to Json"""

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
