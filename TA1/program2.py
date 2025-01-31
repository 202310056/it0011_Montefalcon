#Program 2: Counting the Sum of Digits in a String
string = input("Enter digits from 0 to 9 only: ")

sum = 0

for digit in string:
    if '0' <= digit <= '9':
        sum += int(digit)

print("The sum of digits in the string is: ",sum)