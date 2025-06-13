#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    #pass
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
admin_login("sudo","12345")

def hows_the_weather(temperature):
    # your code here
    pass
    if temperature < 40 :
        return ("It's brisk out there!")
    elif temperature >=40 and temperature <=65 :
        return ("It's a little chilly out there!")
    elif temperature > 85 :
        return ("It's too dang hot out there!")
    else:
        return ("It's perfect out there!")

hows_the_weather(26)

def fizzbuzz(num):
    # your code here
    pass
    if  num%3 == 0 and num%5 == 0 :
        return ("FizzBuzz")
    elif num % 3 == 0 :
        return ("Fizz")
    elif num % 5 ==0:
        return ("Buzz")
    else :
        return (num)
fizzbuzz(45)

def calculator(operation, num1, num2):
    # your code here
    pass
    if operation == "+" :
        return (num1+num2)
    elif operation == "-":
        return (num1-num2)
    elif operation == "*":
        return (num1*num2)
    elif operation == "/":
        return (num1/num2)
    else:
        print("Invalid operation!")
        return None
calculator("-", 23,2)
