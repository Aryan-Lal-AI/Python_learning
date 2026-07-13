# Greetings!
# In the following lines of code I will be practicing typecasting
# Which means converting a variable from one data type to another
# These include str(), int(), float() and bool()
# I will also be handling user input


# To start, I will create 4 variables
first_name = "Aryan"
age = 17
price = 11.99
is_in_middle_school = False

# Now I will type cast each of these to a different data type and print their data types
has_name = bool(first_name)
age = float(age)
price = int(price)
is_in_middle_school = str(is_in_middle_school)

print(type(first_name))
print(type(age))
print(type(price))
print(type(is_in_middle_school))

# As we can see typecasting changed their data types
# Moving on I will now ask for the user's age
# Which I will use to create a basic birth year calculator
# By typecasting the user's age to an integer

user_age = int(input("Please enter your age:"))

# Now I will create a basic if/else statement

if user_age >= 122 or user_age < 0:
    print("sorry please enter a valid age next time")
else:
    birth_year = 2026 - user_age
    print(f"You were born in {birth_year}")

# This was it!
# Thank you for viewing!
