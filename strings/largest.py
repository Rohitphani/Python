n = input("Enter three numbers: ")
x,y,z = n.split(" ")
num1 = int(x)
num2 = int(y)
num3 = int(z)

if num1 > num2 and num1 > num3: 
     print(f"The largest value : {num1}")

elif num2 > num1 and num2 > num3: 
     print(f"The largest value : {num2}")

else:
     print(f"The largest value : {num3}")