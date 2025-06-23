### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email:
    has_been_read = False

    # Declare the class variable, with default value, for emails. 
    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.
Inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():  
    # Create 3 sample emails and add it to the Inbox list. 
    email1 = Email("email1@gmail.com", "Welcome to HyperionDev!", "Thank you for joining.")
    email2 = Email("email2@hotmail.com", "Great work on the bootcamp!", "Congratulations on your progress.")
    email3 = Email("email3@example.com", "Your excellent marks!", "You achieved outstanding results.")
    Inbox.append(email1)
    Inbox.append(email2)
    Inbox.append(email3)


def list_emails(): 
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    for i, email in enumerate(Inbox):
        print(f"{i} {email.subject_line}")


def read_email(num):
    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    if num < len(Inbox):
        email = Inbox[num]
        print(f"\nFrom: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Contents: {email.email_content}")
        email.mark_as_read()
        print(f"Email from {email.email_address} succesfully marked as read.\n")


# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        email_num = int(input("Enter the number of the email you want to read: "))
        read_email(email_num-1)
        
    elif user_choice == 2:
        # add logic here to view unread emails
        print("Unread emails:")
        for i in range(len(Inbox)):
            email = Inbox[i]
            if not email.has_been_read:
                print(f"{i+1}- {email.subject_line}")
            
    elif user_choice == 3:
        # add logic here to quit appplication
        print("Thank you for your time\nQuitting application...")
        break

    else:
        print("ERROR - INVALID INPUT.")

