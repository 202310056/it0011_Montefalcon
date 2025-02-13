fname = input("Enter First Name: ")
lname = input("Enter Last Name: ")
age = input("Enter your age: ")
msg = "Greeting Message: Hello, {}! Welcome. You are {} years old."
str = msg.format(fname[0:3], age)

print("\nFull Name:",fname + " " +lname)
print("Sliced Name:",fname[0:3])
print(str)