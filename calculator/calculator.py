## CALCULATOR ##
print("WELCOME TO MY CALCULATOR\n")

import time

# Solve equations and store in equation history:
def solve(op, num1, num2):
    if op == "+":
        return num1 + num2

    elif op == "-":
        return num1 - num2

    elif op == "*":
        return num1 * num2
    
    elif op == "/":
        try:
            x = (num1 / num2)
            return x 
        except:
            error = ("ERROR, CANNOT DIVIDE BY ZERO")
            return error
            time.sleep(1.5)
    
def store_equation(equation):
    file = None
    try:
        file = open("equations.txt", "a")
        file.write(f"{equation}\n")
    
    except FileNotFoundError as error:
        print("The file you are trying to open does not exist")
        print(error)
        time.sleep(1.5)

    finally:
        if file is not None:
            file.close()
 
# display equation history
def history():
    file = None
    try:
        file = open("equations.txt", "r")
        print(file.read())
        time.sleep(2)
    
    except FileNotFoundError as error:
        print("The file you are trying to open does not exist")
        print(error)
        time.sleep(1.5)

    finally:
        if file is not None:
            file.close()

loop = True
while loop:

# Display Menu:
    try:
        print("""MENU:
        - Press 'ENTER' to calculate an equation
        -  Press 'X' to Exit
        -  Press 'V' to view your equations history 
        """)
        menu = str(input("--> ")).lower()
        if menu == "x":
            loop = False
        
        elif menu == "v":
            history()

        elif menu == "":

# Ask user to enter 2 numbers and store them:
            while True:
                print("\nPlease enter 2 numbers and an operation below:\n")
                try: 
                    numbers = []

                    first_num = int(input("1st number:- "))
                    numbers.append(first_num)

                    second_num = int(input("2nd number:- "))
                    numbers.append(second_num)

                    print(numbers)
                    break

                except:
                    numbers.clear
                    print("ERROR, INVALID INPUT")
                    time.sleep(1.5)


    # Ask user to select operation:
            while True:
                try:
                    operator = input("Please Enter an operator from the follwing operations (+, -, *, /): ")
                    print()
                    if operator == "+" or "-" or "*" or "/":

    # solve and display answer:
                        answer = solve(operator, first_num, second_num)
                        display_answer = (f"{first_num} {operator} {second_num} = {answer}") 
                        store_equation(display_answer)
                        print(display_answer)
                        print()
                        time.sleep(1.5)
                        break
 
                    else:
                        raise(ValueError)
                    
                except:
                    print("ERROR, INVALID OPERATOR")
                    time.sleep(1.5)
        else:
            raise ValueError
    except:
        print("ERROR, INVALID INPUT\n")
        time.sleep(1.5)

    
