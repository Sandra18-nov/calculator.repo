#calculator
number1=eval(input("enter first number: "))
number2=eval(input("enter second number: "))
operator=input("enter operator: ")

def add(num1, num2):
    result=num1 + num2
    print(result)

def subtract(num1, num2):
    result=num1- num2
    print(result)

def divide(num1,num2):
    result=num1/num2
    print(result)

def multiply(num1,num2):
    result=num1*num2
    print(result)

if operator=="+":
    add(number1, number2)


elif operator=="/":
    divide(number1, number2)

elif operator=="-":
    subtract(number1, number2)

elif operator=="*" or operator=="x" or operator=="X":
    multiply(number1, number2)

else:
    print("invalid operator")



