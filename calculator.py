#  different arithematic functions 
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def divide(a,b):
    return a/b
def mod(a,b):
    return a%b
def multiply(a,b):
    return a*b
def floordivision(a,b):
    return a//b
def power(a,b):
    return a**b
while True:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    print()

    print("Press + for adding the numbers")
    print("Press - for subtracting the numbers")
    print("Press / for  dividing the numbers")
    print("Press * for multiplying the numbers")
    print("Press // for taking floor division of  the numbers")
    print("Press % for taking the mod of the numbers")
    print("Press ^ for taking the power of the numbers")
    ch =input("Enter the operator to perform the operation on two numbers")
    if ch in ["/", "//", "%"] and b == 0:
        print("Error: Division by zero is not allowed.")
        continue
    if ch=="+":
        print(f"The Addition of {a} and {b} is {add(a,b)}")
    elif ch=="-":
        print(f"The Subtraction of {a} and {b} is {subtract(a,b)}")
    elif ch=="/":
        print(f"The division of {a} and {b} is {divide(a,b)}")
    elif ch=="*":
        print(f"The multiplication of {a} and {b} is {multiply(a,b)}")
    elif ch=="//":
        print(f"The Floor Division of {a} and {b} is {floordivision(a,b)}")
    elif ch=="%":
        print(f"The  Mod of {a} and {b} is {mod(a,b)}")
    elif ch=="^":
        print(f"The power of {a} with respect to {b} is {power(a,b)}")
    else:
        print("This is a invalid choice. Please enter a valid operator from above ")
        print()
    
    ch=input("Do you want to perform the operations again ? {yes/no or y/n or Yes/No} ").lower()
    if ch not in ["yes","y"]:
        break
    


