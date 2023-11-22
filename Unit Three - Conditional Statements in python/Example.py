#Check if a number is positive
number = int(input("What is your number:"))
if number>0:
    print(f"{number} is positive.")
if number<0:
    print(f"{number} is negative.")

age = int(input("Please enter your age:"))

if age>=18:
    print(f"Someone who is {age} years old can vote.")

if age<18:
    print(f"Someone who is {age} years old is not eligible to vote.")




str = input("Please enter a string:")
if len(str) ==0:
    print("The string is empty")
if len(str) !=0:
    print("The string is not empty.")


def max_number(a, b):
    if a >b:
        return a
    return b

def password_checker(password, user_input):
    return password == user_input

def range_checker(num, lower, upper):
    if lower<=num<=upper:
        return True
    return False

a=int(input("Please enter a number between 1 and 10"))
if range_checker(a, 1, 10):
    print("This number is in between 1 and 10")

if range_checker(a, 1, 10)==False:
    print("Ur either stupid or vinayak")