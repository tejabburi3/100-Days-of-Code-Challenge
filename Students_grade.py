
print("Student Report Card Generator ")


name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")
course = input("Enter Course/Class: ")
sub=[]
print("\nEnter marks for 5 subjects (out of 100):")
for i in range(1,6):
    sub.append(int(input(f'Enter Subject{i} Marks : ')))


total = sum(sub)
average = total / 5


if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "Fail"


print("---------------")
print(f"Name       : {name}")
print(f"Roll No    : {roll}")
print(f"Class      : {course}")
print("---------------------------")
print(f"Total Marks: {total}/500")
print(f"Average    : {average:.2f}")
print(f"Grade      : {grade}")

