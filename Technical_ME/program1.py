f=open('Technical_ME\\numbers.txt', 'r')
lines = f.readlines()
f.close()

line_number = 1
for line in lines:
    numbers = line.strip().split(',')
    total_sum = sum(int(num) for num in numbers)
    
    if str(total_sum) == str(total_sum)[::-1]:
        result = "Palindrome"
    else:
        result = "Not a Palindrome"

    print(f"Line {line_number}: {','.join(numbers)} (sum {total_sum}) - {result}")
    line_number += 1