def divide(num1, num2):
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        return None
    return num1 / num2

def exponentiate(num1, num2):
    return num1 ** num2

def remainder(num1, num2):
    if num2 == 0:
        print("Error: Cannot divide by zero for remainder.")
        return None
    return num1 % num2

def summation(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    if num1 >= num2:
        print("Error: The second number must be greater than the first.")
        return None
    return sum(range(num1, num2 + 1))

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def menu():
    while True:
        print("\nMenu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").upper()
        
        if choice == 'Q':
            print("Goodbye!")
            break
        
        elif choice == 'D':
            num1 = get_float_input("Enter the first number (numerator): ")
            num2 = get_float_input("Enter the second number (denominator): ")
            result = divide(num1, num2)
            if result is not None:
                print(f"Result: {result}")
        
        elif choice == 'E':
            num1 = get_float_input("Enter the base number: ")
            num2 = get_float_input("Enter the exponent: ")
            result = exponentiate(num1, num2)
            print(f"Result: {result}")
        
        elif choice == 'R':
            num1 = get_float_input("Enter the first number: ")
            num2 = get_float_input("Enter the second number (denominator): ")
            result = remainder(num1, num2)
            if result is not None:
                print(f"Result: {result}")
        
        elif choice == 'F':
            num1 = get_float_input("Enter the first number (lower limit): ")
            num2 = get_float_input("Enter the second number (upper limit): ")
            result = summation(num1, num2)
            if result is not None:
                print(f"Result: {result}")
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()