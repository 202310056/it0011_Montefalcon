lname = input("Enter Last Name: ")
fname = input("Enter First Name: ")
age = input("Enter your age: ")
cnum = input("Enter your contact number: ")
course = input("Enter your course: ")

lines = ["\nLast Name: ",lname,"\nFirst Name: ",fname,"\nAge: ",age,"\nContact Number: ",cnum,"\nCourse: ",course]
f=open("students.txt", "a")
f.writelines(lines)
f.close()

print("\nLast Name: ",lname)
print("First Name: ",fname)
print("Age: ",age)
print("Contact Number: ",cnum)
print("Course: ",course)
print("Student information has been saved to 'students.txt'.")