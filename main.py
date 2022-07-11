art = """

                       .
                        `:.
                          `:.
                  .:'     ,::
                 .:'      ;:'
                 ::      ;:'
                  :    .:'
                   `.  :.
          _________________________
         : _ _ _ _ _ _ _ _ _ _ _ _ :
     ,---:".".".".".".".".".".".".":
    : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
    `.`.  `:-===-===-===-===-===-:'
      `.`-._:                   :
        `-.__`.               ,' met.
    ,--------`"`-------------'--------.
     `"--.__                   __.--"'
            `""-------------""'



"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def printing_report(new_dict):
    dictionary = {}
    for key in new_dict:
        if key != "money":
            dictionary[key] = str(new_dict[key]) + "ml"
        else:
            dictionary[key] = "$" + str(new_dict[key])
    print(dictionary)


def checking_resources(users_choice):
    no_of_items = 0
    for each_items in MENU[users_choice]["ingredients"]:
        if MENU[users_choice]["ingredients"][each_items] <= resources[each_items]:
            resources[each_items] = resources[each_items] - MENU[users_choice]["ingredients"][each_items]
            no_of_items += 1
        else:
            no_of_items = 0
            break
    return no_of_items


def deducting_report(users_choice, reports):
    for each_items in MENU[users_choice]["ingredients"]:
        if MENU[users_choice]["ingredients"][each_items] <= resources[each_items]:
            reports[each_items] = reports[each_items] - MENU[users_choice]["ingredients"][each_items]
        else:
            break
    return reports


# TODO.1:Ask the user what they want to try and it ask everytime until a machine is turn switch off.
User_Choice = "on"
report = resources
report["money"] = 0
print(art)
while User_Choice != "off":
    choice = input("What would you like? (espresso/latte/cappuccino/): ")
    if choice == "off":
        break
    # TODO.2: If user ask to print report,program should display the report of items available.
    if choice != "report":
        available = checking_resources(choice)
        if available >= 2:
            report = deducting_report(choice, report)
            print("Insert the coins")
            quarters = int(input("No of quarters: "))
            dimes = int(input("No of dimes: "))
            nickel = int(input("No of nickels: "))
            pennies = int(input("No of pennies: "))
            money_paid_by_user = round(0.25 * quarters + 0.10 * dimes + 0.05 * nickel + 0.01 * pennies)
            money_required = MENU[choice]["cost"]
            if money_paid_by_user == money_required:
                report["money"] += money_required
                print(f"Here is your {choice} ☕. Enjoy!")
            elif money_paid_by_user > money_required:
                remaining_amount = money_paid_by_user - money_required
                print(f"Here is ${remaining_amount} in change.")
                report["money"] += money_required
                print(f"Here is your {choice} ☕. Enjoy!")
        else:
            print(f"Sorry resources not available for making {choice}")
            continue
    else:
        printing_report(report)


