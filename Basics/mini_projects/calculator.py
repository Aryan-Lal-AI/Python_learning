# Greetings!
# In the following lines of code I will be creating a very basic calculator
# I will do so in order to practice if/else statements

response = input(
    "Would you like to calculate more than 2 numbers(YES/NO)? ").upper().strip()
number_1 = float(input("Please enter a number: "))
number_2 = float(input("Please enter another number: "))
operator = input("Please enter the mathematical operation(+, -, *, /): ")

if response == "NO":
    if operator == "+":
        print(f"The total of your numbers is: {number_1 + number_2}")
    elif operator == "-":
        print(f"The difference of your numbers is: {number_1 - number_2}")
    elif operator == "*":
        print(f"The product of your numbers is: {number_1 * number_2}")
    elif operator == "/":
        if number_2 == 0:
            print("You cannot divide by zero!")
        else:
            print(f"The quotient of your numbers is: {number_1 / number_2}")
    else:
        print(f"{operator} isn't a valid operator! ")
elif response == "YES":
    print("Unfortunately this calculator calculates only two numbers at a time.")
else:
    print("You didn't enter a valid response! ")

# This was it!
# Thank you for viewing!
