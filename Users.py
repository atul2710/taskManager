import bcrypt
import json
import os

'''
Module for methods on user
'''

users = {}
data_folder = 'data'
users_file = 'users.json'
user_file_path = os.path.join(data_folder, users_file)
current_user = None

'''
Method to load users
'''
def load_users():
    global users
    #check if the file data/user.json exist 
    #if file doesn't exit, create a file
    #if file exist, load the users to the user dict
    print ("Loading users.....")
    if os.path.exists(user_file_path):
        with open(user_file_path, 'r') as file:
            data = file.read()
            users = json.loads(data)
    else:
        print("No users found..")
        print("Please add new user and continue...")
        with open(user_file_path, "w") as file:
            file.write("{}")
            file.close()
        
'''
Method to validate user
'''
def validate_user_credentials(username, password):
    global current_user
    print("Validating user")
    if (username in users):
        print ("Valid user found, validataing password")
        #validate password
        if(validate_password(username, password)):
            print ("User authenticated")
            current_user = username
            return True
        else:
            print ("Invalid password")
    else :
        print ("User not found!!! Try again!!")
    return False

'''
Method to hash password
'''
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    #convert to string
    hashed_password = hashed_password.decode()
    return hashed_password

'''
Method to add new user
'''
def add_user(username, password):
    if(username not in users):
        users[username] = hash_password(password)
        print("User added successfully")
        save_users()
        return True
    else:
        print("User already exists")
        return False
    
'''
Method to validate password
'''
def validate_password(username, hashed_password):
    stored_hashed_password = users[username]
    password = hashed_password.encode()
    if bcrypt.checkpw(password, stored_hashed_password.encode()):
        print("Password is valid")
        return True
    else:
        print("Invalid password")
    return False

'''
Method to save users to users.json. Call this method after adding new user
'''
def save_users():
    # write users to users.json
    with open(user_file_path, 'w') as file:
        file.write(json.dumps(users))
        file.close()
        print ("Users saved successfully")