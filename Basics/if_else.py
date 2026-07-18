# Greetings!
# Today I will be practicing if/else statements
# I will create a basic age checker to determine if the user is eligible to obtain a driver's license

age = int(input("Please enter your real age in digits: "))

if age > 122 or age < 0:
    print("Please enter a valid age.")
elif age >= 70:
    print("Unfortunately you are too old to obtain a driving license.")
elif age < 18:
    print("Unfortunately you are too young to obtain a driving license.")
else:
    print("You are eligible to obtain a driving license!")

# This was it!
# Thank you for viewing!
