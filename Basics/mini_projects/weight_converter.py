# Hello!
# Today I will be creating a very basic weight converter program
# This program will convert kg to lbs and lbs to kg
# This will help me practice if/else statements and user input
kg_to_lbs_ratio = 2.205
unit = input("Please enter your weight unit (KG/LBS): ").upper()

if unit == "KG":
    weight = float(input(f"Please enter your weight in {unit} using digits: "))
    print(
        f"Your weight in pounds is: {round(weight * kg_to_lbs_ratio, 2)} lbs")
elif unit == "LBS":
    weight = float(input(f"Please enter your weight in {unit} using digits: "))
    print(
        f"Your weight in kilograms is: {round(weight / kg_to_lbs_ratio, 2)} kg")
elif unit == "":
    print("You didn't type a response! ")
else:
    print(f"{unit} isn't a valid unit!")

# This was it!
# Thank you for viewing!
