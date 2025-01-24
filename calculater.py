num1 = int(input("Enter the first number: "))
operation = input("Choose operation (+, -, *, /, **, %): ")
num2 = int(input("Enter the second number: "))


if operation == "+":
    result = num1 + num2 
elif operation == "-":
    result = num1 - num2 
elif operation == "*":
    result = num1 * num2 
elif operation == "/":
    result = num1 / num2
elif operation == "**":
    result = num1 ** num2
elif operation == "%":
    result = num1 % num2 


else:
    result = "Invalid operation"

print("The result is: " + str(result))       
