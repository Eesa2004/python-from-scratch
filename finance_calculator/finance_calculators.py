import math

# enter details of your interest:
def interest_details():
    valid = False
    while not valid:
        try:
            deposit = float(input("Please enter the amount of money you are depositing: "))
            if deposit > 0:
                valid = True
            else:
                print("ERROR, CAN'T HAVE A NEGATIVE DEPOSIT.\n")
        except:
            print("ERROR, PLEASE USE NUMBERS ONLY\n")

    valid = False
    while not valid:
        try:
            interest_rate = float(input("Please enter your interest rate without the '%' sign: "))
            valid = True
        except:
            print("ERROR, PLEASE USE NUMBERS ONLY\n")

    valid = False
    while not valid:
        try:
            years = float(input("Please enter the number of years you plan to invest for: "))
            if years > 0:
                valid = True
            else:
                print("ERROR, CAN'T HAVE NEGATIVE YEARS.\n")
        except:
            print("ERROR, PLEASE USE NUMBERS ONLY\n")

    valid = False
    print()
    while not valid:
        print("Does your invesment have simple interest or compund interest?")
        try:
            interest_type = input("Enter either 'simple' or 'compound' to proceed: ")
            if interest_type.lower() == "simple":
                valid = True
                print()
                simple(deposit, interest_rate, years)
            elif interest_type.lower() == "compound":
                valid = True
                print()
                compound(deposit, interest_rate, years)
            else:
                print("ERROR\n")
        except:
            pass

# enter details of bond:
def bond_details():
    valid = False
    while not valid:
        try:
            house_value = float(input("Please enter the present value of your house: "))
            if house_value > 0:
                valid = True
            else:
                print("ERROR, CAN'T HAVE A NEGATIVE VALUE.\n")
        except:
            print("ERROR, PLEASE USE NUMBERS ONLY\n")

    valid = False
    while not valid:
        try:
            interest_rate = float(input("Please enter your annual interest rate without the '%' sign: "))
            interest_rate = (interest_rate/100)/12
            valid = True
        except:
            print("ERROR, PLEASE USE NUMBERS ONLY\n")

    valid = False
    while not valid:
        try:
            no_of_months = float(input("Please enter the number of months you plan to invest for: "))
            if no_of_months > 0:
                valid = True
            else:
                print("ERROR, CAN'T HAVE NEGATIVE MONTHS.\n")
        except:
            print("ERROR, PLEASE USE NUMBERS ONLY\n")

    valid = False
    print()
    repayment(house_value, interest_rate, no_of_months)

# calculate compound interest:
def compound(p, r, t):
    interest = p*math.pow((1+(r/100)),t)
    input(f"After {t} years of interest your total amount of investment will be: £{interest}\nPress ENTER to proceed:")
    print()

# calculate simple interest:
def simple(p, r, t):
    interest = p+(p*(r/100)*t)
    input(f"After {t} years of interest your total amount of investment will be: £{interest}\nPress ENTER to proceed:")
    print()

# caculate monthly repayment of bond:
def repayment(p, i, n):
    bond = (i * p)/(1 - (1 + i)**(-n))
    input(f"your monthly repayment towards your home loan will be: £{bond}\nPress ENTER to proceed:")
    print()

# main code:
valid = False

# menu;
print()
print("WELCOME TO YOUR VERY OWN FINANCIAL CALCULATOR\n")

while not valid:
    print("MENU CHOICES:")
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond - to calculate the amount you'll have to pay on a home loan")
    print("exit - to exit financial calculator")
    try:
        answer = input("\nEnter either 'investment', 'bond' or 'exit' from the menu above to proceed:")
        print()
        if answer.lower() == "investment":
            interest_details()
        elif answer.lower() == "bond":
            bond_details()
        elif answer.lower() == "exit":
            valid = True
            print("Thank you for using this financial calculator\n")
        else:
            print("ERROR\n")
    except:
        pass
        