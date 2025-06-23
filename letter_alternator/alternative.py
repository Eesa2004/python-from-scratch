import time
#INTRODUCTION:
input("Hi there,\nThis program is designed to alternate every other letter/word into capital letters.\nPlease press 'ENTER' to proceed... ")
print()

#Find if number is even or not:
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

#Function to alternate every other letter:
def alt_letter(string):
    new_string = ""
    for i in range(len(string)):
        if is_even(i):
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()

    print(f"\nYour alternated string is: {new_string}\n")
    time.sleep(1.5)

#Function to alternate every other word:
def alt_word(string):
    split = string.split()
    new_string = ""
    for i in range(len(split)):
        if is_even(i):
            new_string += split[i].upper()
        else:
            new_string += split[i].lower()
        new_string += " "

    print(f"\nYour alternated string is: {new_string}\n")
    time.sleep(1.5)


while True:
    #MAIN MENU:
    choice = input("""      MENU OPTIONS:
    1 - Alternate every other letter
    2 - Alternate every other word
    3 - QUIT
    
    Please Enter your choice here:- """)
    print()
    
    if choice == "3":
        break

    elif choice == "2":
        while True:
            string = input("Please Enter a word or sentence: ").lower()
            strip_string = string.strip()
            if strip_string == "":
                print("\nDo not leave blank\n")
                time.sleep(1.5)
            elif strip_string[0] == " ":
                print("\nDo not leave blank\n")
                time.sleep(1.5)
            else:
                alt_word(string)
                break
        
    elif choice == "1":
        while True:
            string = input("Please Enter a word or sentence: ").lower()
            strip_string = string.strip()
            if strip_string == "":
                print("\nDo not leave blank\n")
                time.sleep(1.5)
            elif strip_string[0] == " ":
                print("\nDo not leave blank\n")
                time.sleep(1.5)
            else:
                alt_letter(string)
                break

    else:
        print("NOT A VALID CHOICE")
        print()
        time.sleep(1.5)