print("CREATE A REGISTER FORM FOR AN EXAM VENUE:\n")
input("Press 'ENTER' to proceed:- ")

#get number of students:
number_of_students = int(input("Please enter how many students are registering as an integer:- "))

#create register form:
with open("reg_form.txt", "w") as file:
    file.write("Student ID Number        Signiture\n")

    for i in range(number_of_students):
        ID_number = input(f"Student {i+1}, Please enter your ID number:- ")
        file.write(f"\n\n{ID_number}                     ....................\n")


with open("reg_form.txt", "r") as file:
    form = file.read()
    print("Thank you for crreating a register form for your exam venue,\nhere's your form\n")
    print(form)