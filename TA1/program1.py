#Program 1: Counting Vowels, Consonants, Spaces, and Other Characters in a String
string = input("Enter a string: ")

vowels = 0
consonants = 0
spaces = 0
other_char = 0

vowels_list = ['A','E','I','O','U','a', 'e', 'i', 'o', 'u']

for char in string:
    if char in vowels_list:
            vowels += 1
    elif ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
            consonants += 1
    elif char == ' ':
        spaces += 1
    else:
        other_char += 1
        
print("The string consists of ", vowels,"vowels, ", consonants, "consonants, ", spaces, "spaces, and ", other_char, "other characters.")