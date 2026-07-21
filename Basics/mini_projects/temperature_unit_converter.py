# Hello!
# In this file I will create a simple temperature converter
# This will convert celsius, fahrenheit and kelvin

temperature = float(input("Please enter the temperature: "))
unit = (input("Please enter the unit of your temperature(C for Celsius,F for Fahrenheit and K for Kelvin): ")).upper().strip()
new_unit = input(
    "Please enter the unit you'd like to convert your temperature to(C for Celsius,F for Fahrenheit and K for Kelvin): ").upper().strip()

if unit == new_unit:
    print("This operation is invalid!")
elif unit == "C":
    if new_unit == "F":
        print(
            f"Your temperature is: {(temperature * 9/5) + 32:.1f} Fahrenheit.")
    elif new_unit == "K":
        print(f"Your temperature is: {temperature + 273.15:.1f} Kelvin. ")
    else:
        print(f"{new_unit} is not a valid unit!")
elif unit == "F":
    if new_unit == "C":
        print(f"Your temperature is: {(temperature - 32) * 5/9:.1f} Celsius.")
    elif new_unit == "K":
        print(
            f"The temperature is: {(temperature - 32) * 5/9 + 273.15:.1f} Kelvin.")
    else:
        print(f"{new_unit} is not a valid unit!")
elif unit == "K":
    if new_unit == "C":
        print(f"Your temperature is: {temperature - 273.15:.1f} Celsius.")
    elif new_unit == "F":
        print(
            f"Your temperature is: {(temperature - 273.15) * 9/5 + 32:.1f} Fahrenheit")
    else:
        print(f"{new_unit} is not a valid unit!")
else:
    print(f"{unit} isn't a valid unit! ")

# Thank you for viewing!
