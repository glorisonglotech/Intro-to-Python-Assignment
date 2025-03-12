num1 = int(input("Enter the first number "))
operator = input("Enter a mathematical operator (+,-,*,/) ")
num2 = int(input("Enter the second number "))
print("\n")
print("***************************************")


if operator == "+":
    print(f"The sum of {num1} + {num2} is: " ,(num1 + num2))
elif operator == "-":
    print(f"The difference of {num1} - {num2} is: ",(num1 - num2))
elif operator == "*":
    print(f"The product of {num1} * {num2} is :",(num1 * num2))
elif operator == "/":
    if num2 != 0:
        print(f"The division of {num1} / {num2} is : ",(num1 / num2))
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator")

print("***************************************")