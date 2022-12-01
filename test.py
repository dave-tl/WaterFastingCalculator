class Calculations:
    wfc_multiplication = [0.85, 1.90, 2.72, 3.41, 4.02, 4.58, 5.09, 5.57, 6.02, 6.45, 6.85, 7.24,
                          7.62, 7.98, 8.33]
    user_weight = 85
    user_goal = 24

    def weight_loss_calc(form_wfc, user_weight, user_goal):
        if user_goal < 16:
            weight_loss = (user_weight / 100 * float(form_wfc[user_goal - 1]))
        else:
            multiplier_past_15 = 8.33 + ((user_goal - 15) * 0.32)
            weight_loss = (user_weight / 100 * float(multiplier_past_15))
        return weight_loss

    print(weight_loss_calc(form_wfc=wfc_multiplication, user_weight=user_weight, user_goal=user_goal))
