import os
import getpass
import Users as us
import Task as ts
# main program




'''
Method to display the the start menu
'''
def start_menu():
    print("Plese select your option:")
    print ("\t1. Enter 1 for New User Registration")
    print ("\t2. Enter 2 for Existing User")
    print ("\t3. Enter 3 to exit the application")

'''
Method to display user menu 
 '''   
def user_menu():
    print("Plese select your user option:")
    print ("\t1. Enter 1 to View Task")
    print ("\t2. Enter 2 to Add Task")
    print ("\t3. Enter 3 to Update Task")
    print ("\t4. Enter 4 to Delete Task")
    print ("\t5. Enter 5 to Exit the application")
    
def login():
    username = input("Enter username: ")
    password = input("Enter password")
    us.validate_user_credentials(username, password)


######################################

#   Main program   #

######################################
# check if the data folder exist
if not os.path.exists(us.data_folder):
    os.makedirs('data')
# load users
us.load_users()

# Display start menu
start_menu()
option = input ("Enter your option: ")
match option:
    case '1':
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        us.add_user(username, password)
    case '2':
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        if(us.validate_user_credentials(username, password)):
            while True:
                user_menu()
                option = input ("Enter your option: ")
                match option:
                    case '1':
                        print ("View Task")
                        ts.view_tasks()
                    case '2':
                        print ("Add Task")
                        task_description = input("Enter task description: ")
                        ts.add_task(task_description)
                    case '3':
                        print ("Update Task")
                        task_id = input("Enter task id: ")
                        status = input("Enter status: ")
                        ts.update_task(task_id, status)
                    case '4':
                        print ("Delete Task")
                        task_id = input("Enter task id: ")
                        ts.delete_task(task_id)
                    case '5':
                        print ("Exiting Application")
                        break
                    case _:
                        print ("Invalid option!!")
    case '3':
        print ("Exiting Application")
    case _:
        print ("Invalid option!!")