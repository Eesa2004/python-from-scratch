# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#==================IMPORTING LIBRARIES===================
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"


#===================READ IN ALL TASKS====================
# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#=========================DEFINING FUNCTIONS=============================

#Register new user and add it to the user.txt file
def reg_user():
    # - Request input of a new username
    while True:
        try:
            new_username = input("New Username: ")
            if new_username in username_password:
                raise ValueError
            else:
                break
        
        except:
            print("Sorry, this username alreasy exists :(\nPlease try a different Username\n")

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password
        
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")


#Allow a user to add a new task to task.txt file
def add_task():
    '''Prompt a user for the following: 
        - A username of the person whom the task is assigned to,
        - A title of a task,
        - A description of the task and 
        - the due date of the task.'''
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


#View all tasks
def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling)'''
    x = 1
    for t in task_list:
        disp_str = f"--------------------TASK No. {x}--------------------\n"
        disp_str += f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Complete?:  Yes\n" if t['completed'] else "Task Complete?:  No\n"
        disp_str += f"Task Description: \n {t['description']}"
        print(f"{disp_str}\n---------------------------------------------------\n")
        x += 1
    input("Press 'ENTER' to continue...")


#View and edit tasks for current logged in user only
def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing, numbering
        and labelling)'''
    x = 1
    print(f"\nHere are all of your tasks:\n")
    user_task_list = []
    for t in task_list:
        if t['username'] == curr_user:
            user_task_list.append(t)
            disp_str = f"--------------------TASK No. {x}--------------------\n"
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Complete?:  Yes\n" if t['completed'] else "Task Complete?:  No\n"
            disp_str += f"Task Description: \n {t['description']}"
            print(f"{disp_str}\n---------------------------------------------------\n")
            x += 1

    #Create Sub Menu to manage and edit users tasks
    while True:
        try:
            task_num = int(input("""
            Please choose a following Option below:
            >>> Enter the number of the task you would like to select and change.
            >>> Enter -1 to Return to Main Menu.
            : """))
            if task_num == -1:
                break
            elif task_num < 1:
                raise IndexError
            else:
                (user_task_list[task_num-1])['completed']

            task_menu = input("""
            Please Enter a following Option below:
            m - Mark the task as complete/incomplete
            e - Edit the task
            : """).lower()

            if task_menu == "m":
                while True:
                    try:
                        if (user_task_list[task_num-1])['completed'] == True:
                            mark_complete = input("""
                            This task is already completed, Would you like to mark it as incomplete?
                            y - Yes
                            n - No
                            Press y or n: """).lower()
                            if mark_complete == "y":
                                (user_task_list[task_num-1])['completed'] = False
                                i = 0
                                for t in task_list:
                                    if t['username'] == curr_user:
                                        t = user_task_list[i]
                                        i += 1
                                with open("tasks.txt", "w") as task_file:
                                    task_list_to_write = []
                                    for t in task_list:
                                        str_attrs = [
                                            t['username'],
                                            t['title'],
                                            t['description'],
                                            t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                            t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                            "Yes" if t['completed'] else "No"]
                                        task_list_to_write.append(";".join(str_attrs))
                                    task_file.write("\n".join(task_list_to_write))
                                print("\nTask successfully marked as incomplete.\n")
                                break

                            elif mark_complete == "n":
                                break

                            else:
                                raise ValueError
                            
                        elif (user_task_list[task_num-1])['completed'] == False:
                            mark_complete = input("""
                            This task is incompleted, Would you like to mark it as complete?
                            y - Yes
                            n - No
                            Press y or n: """).lower()
                            if mark_complete == "y":
                                (user_task_list[task_num-1])['completed'] = True
                                i = 0
                                for t in task_list:
                                    if t['username'] == curr_user:
                                        t = user_task_list[i]
                                        i += 1
                                with open("tasks.txt", "w") as task_file:
                                    task_list_to_write = []
                                    for t in task_list:
                                        str_attrs = [
                                            t['username'],
                                            t['title'],
                                            t['description'],
                                            t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                            t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                            "Yes" if t['completed'] else "No"]
                                        task_list_to_write.append(";".join(str_attrs))
                                    task_file.write("\n".join(task_list_to_write))
                                print("\nTask successfully marked as complete.\n")
                                break

                            elif mark_complete == "n":
                                break

                            else:
                                raise ValueError
                    
                    except ValueError:
                        print("\nNOT A VALID OPTION")

            elif task_menu == "e":
                if (user_task_list[task_num-1])['completed'] == True:
                    print("\nSorry, Cannot edit this task as it is already completed.")
                else:
                    while True:
                        try:
                            edit_menu = input("""
                            Please Enter a following Option below:
                            u - Change the username of the person to whom the task is assigned
                            d - Change the due date of the task
                            : """).lower()

                            if edit_menu == "u":
                                change_user = input("\nUsername of new person assigned to task: ")

                                if change_user not in username_password.keys():
                                    raise TypeError
                                
                                elif (user_task_list[task_num-1])['username'] == change_user:
                                    raise KeyError
                                
                                else:
                                    (user_task_list[task_num-1])['username'] = change_user
                                    i = 0
                                    for t in task_list:
                                        if t['username'] == curr_user:
                                            t = user_task_list[i]
                                            i += 1
                                    with open("tasks.txt", "w") as task_file:
                                        task_list_to_write = []
                                        for t in task_list:
                                            str_attrs = [
                                                t['username'],
                                                t['title'],
                                                t['description'],
                                                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                                "Yes" if t['completed'] else "No"]
                                            task_list_to_write.append(";".join(str_attrs))
                                        task_file.write("\n".join(task_list_to_write))
                                    print(f"\nTask successfully assigned to '{change_user}'.\n")
                                    break

                            elif edit_menu == "d":

                                change_due_date = input("\nNew due date of task (YYYY-MM-DD): ")
                                change_due_date = datetime.strptime(change_due_date, DATETIME_STRING_FORMAT)
                                
                                if (user_task_list[task_num-1])['due_date'] == change_due_date:
                                    raise TabError
                                
                                else:
                                    (user_task_list[task_num-1])['due_date'] = change_due_date
                                    i = 0
                                    for t in task_list:
                                        if t['username'] == curr_user:
                                            t = user_task_list[i]
                                            i += 1
                                    with open("tasks.txt", "w") as task_file:
                                        task_list_to_write = []
                                        for t in task_list:
                                            str_attrs = [
                                                t['username'],
                                                t['title'],
                                                t['description'],
                                                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                                "Yes" if t['completed'] else "No"]
                                            task_list_to_write.append(";".join(str_attrs))
                                        task_file.write("\n".join(task_list_to_write))
                                    print(f"\nDue date successfully changed to '{change_due_date}'.\n")
                                    break

                            else:
                                raise NameError
                                    
                        except NameError:
                            print("\nNOT A VALID OPTION")

                        except TypeError:
                            print("\nUSER DOES NOT EXIST")

                        except KeyError:
                            print(f"\n'{change_user}' is already assigned to this task")

                        except ValueError:
                            print("\nINVALID DATETIME FORMAT. Please use the format specified")

                        except TabError:
                            print ("\nDUE DATE IS ALREADY SET AS THAT")

            else:
                raise TypeError

        except IndexError:
            print("\nNOT A VALID TASK NUMBER")

        except ValueError:
            print("\nPLEASE USE NUMBERS ONLY")

        except TypeError:
            print("\nNOT A VALID OPTION")


#generate two reports about task and users containing useful information    
def generate_reports():
    #task_overview report
    num_tasks = len(task_list)
    completed_tasks = 0
    incompleted_tasks = 0
    overdue = 0
    for t in task_list:
        if t['completed'] == False:
            incompleted_tasks += 1
            if t['due_date'].date() < date.today():
                overdue += 1
        else:
            completed_tasks += 1
    incomplete_percent = (incompleted_tasks/(num_tasks))*100
    overdue_percent = (overdue/(num_tasks))*100

    with open("task_overview.txt", "w") as file:
        file.write(f"""Task_overview Report:
                                                         
    Total number of tasks generated and tracked: {num_tasks}
    Total number of completed tasks:             {completed_tasks}
    Total number of uncompleted tasks:           {incompleted_tasks}
    Total number of tasks overdue:               {overdue}
    Percentage of tasks that are incomplete:     {incomplete_percent}%
    Percentage of tasks that are overdue:        {overdue_percent}%
    """)

    with open("task_overview.txt", 'r') as task_overview:
        report = task_overview.read()
        print(f"""------------------------------------------------------------------
{report}
------------------------------------------------------------------\n""")

    #user_overview report
    num_users = len(username_password.keys())
    user_tasks = 0
    user_incomplete_tasks = 0
    user_complete_tasks = 0
    user_overdue = 0
    for t in task_list:
        if t['username'] == curr_user:
            user_tasks += 1
            if t['completed'] == False:
                user_incomplete_tasks += 1
                if t['due_date'].date() < date.today():
                    user_overdue += 1
            else:
                user_complete_tasks += 1
    user_tasks_percent = (user_tasks/(num_tasks))*100
    user_complete_percent = (user_complete_tasks/(user_tasks))*100
    user_incomplete_percent = (user_incomplete_tasks/(user_tasks))*100
    user_overdue_percent = (user_overdue/(user_tasks))*100

    with open("user_overview.txt", "w") as file:
        file.write(f"""Personal User_overview Report:
                   
    Username:                                    {curr_user}
    Total number of users registered:            {num_users}             
    Total number of tasks generated and tracked: {num_tasks}
    Total number of tasks assigned to you:       {user_tasks}
    Percentage of your tasks from total:         {user_tasks_percent}%
    Percentage of your tasks completed:          {user_complete_percent}%
    Percentage of your tasks incompleted:        {user_incomplete_percent}%
    Percentage of your tasks overdue:            {user_overdue_percent}%
    """)

    with open("user_overview.txt", 'r') as user_overview:
        report = user_overview.read()
        print(f"""------------------------------------------------------------------
{report}
------------------------------------------------------------------\n""")
    
    input("Press 'ENTER' to continue...")



#=============================LOGIN SECTION=============================
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
         generate_reports()

    elif menu == 'ds' and curr_user != 'admin':
        print("\nSorry, only the admin can access this.")
    
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        # num_users = len(username_password.keys())
        # num_tasks = len(task_list)
        with open("user.txt", 'r') as user_file:
            user_data = user_file.read().split("\n")

        with open("tasks.txt", 'r') as task_file:
            task_data = task_file.read().split("\n")
            task_data = [t for t in task_data if t != ""]

        print("-----------------------------------")
        print(f"Number of users: \t\t {len(user_data)}")
        print(f"Number of tasks: \t\t {len(task_data)}")
        print("-----------------------------------")  

        input("\nPress 'ENTER' to continue...")


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")