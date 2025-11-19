name  = input("Give a string: ")

reverse = name[::-1]

if reverse == name:
    print("It is a palindrome")
else:
    print("Its not a palindrome")
