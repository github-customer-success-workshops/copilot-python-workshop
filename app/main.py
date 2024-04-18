from calculator import Calculator

calculator = Calculator()

num1 = float(input("Enter first number: "))

operation = input("Enter operation (+, -, *, /): ")

num2 = float(input("Enter second number: "))

if operation == '+':
    print("Result: ", calculator.add(num1, num2))
elif operation == '-':
    print("Result: ", calculator.subtract(num1, num2))
elif operation == '*':
    print("Result: ", calculator.multiply(num1, num2))
elif operation == '/':
    print("Result: ", calculator.divide(num1, num2))
else:
    print("Invalid operation!")