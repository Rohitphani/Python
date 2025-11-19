m = int(input("Marks in maths: "))
s = int(input("Marks in science: "))
e = int(input("Marks in english: "))

total_marks = (m+s+e)
avg = total_marks/3

percentage = (total_marks/300)*100
grade = ""

if percentage > 90: 
    grade = "A"
elif percentage > 80 and percentage <= 90:
    grade = "B"
elif percentage > 70 and percentage <= 80:
    grade = "C"
else:
    grade = "PASS"


print(f"Total marks: {total_marks} \nPercentage: {percentage} \nGrade:{grade}")