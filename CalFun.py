def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice (1-4): "))
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if choice == 1:
    print("Result:", add(x, y))
elif choice == 2:
    print("Result:", subtract(x, y))
elif choice == 3:
    print("Result:", multiply(x, y))
elif choice == 4:
    print("Result:", divide(x, y))
else:
    print("Invalid choice")
