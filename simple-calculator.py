# A simple Calculator
operator = input("Do you want to add, subtract, multiply or divide? ")

num1 = float(input("Put in the first number "))

num2 = float(input("Put in the second number "))



if operator == "add":
    sum = num1 + num2
    print("Answer is " + str(sum))

elif operator == "subtract":
    diff = num1 - num2
    print("Answer is " + str(diff))

elif operator == "multiply":
    product = num1 * num2
    print("Answer is " + str(product))

elif operator == "divide":
    quotient = num1 / num2
    print("Answer is " + str(quotient))