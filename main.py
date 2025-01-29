from random import choice

import art

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

commands = {
    "+" : add ,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(art.logo)
    move_forward = True
    num_1 = float(input("what is your first number = "))
    while move_forward:
        for symbols in commands:
            print(symbols)
        operation = input("what operation to perform :- ")
        num_2 = float(input("what is your second number = "))
        answer = commands[operation](num_1,num_2)

        print(f"{num_1}{operation}{num_2} = {answer}")

        choices = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()


        if choices == "y":
            num_1 = answer

        else:
            move_forward =False
            print(f"your answer is {answer}")
            print("\n " * 60)
            calculator()

calculator()