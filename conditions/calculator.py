num1 = int(input("Give num1 value: "))
num2 = int(input("Give num2 value: "))
operator = input("Give operator: ")

if operator == "+":
    print(f"Addition of two numbers are {num1+num2}")

elif operator == "-":
    print(f"Subraction of two numbers are {num1-num2}")

elif operator == "*":
    print(f"Multipliaction of two numbers are {num1*num2}")

elif operator == "/":
    print(f"Division of two numbers are {num1/num2}")
    
else:
    print("Invalid operator.")
