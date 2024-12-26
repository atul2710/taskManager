import json
import os
import Users as us

class Task:
    def __init__(self, description):
        self.description = description
        self.status = 'Pending'

current_user_tasks = None
task_file = 'tasks.json'
task_file_path = None

'''
Method to load tasks
'''
def load_tasks():
    global current_user_tasks
    global task_file_path
    #check if the file data/{current_user}_tasks.json exist 
    #if file doesn't exit, create a file
    #if file exist, load the tasks to the task dict
    print ("Loading tasks.....")
    if task_file_path is None:
        task_file_name = us.current_user + '_' + task_file
    task_file_path = os.path.join(us.data_folder, task_file_name)
    if os.path.exists(task_file_path):
        with open(task_file_path, 'r') as file:
            data = file.read()
            if data == "":
                current_user_tasks = {}
            else:
                current_user_tasks = json.loads(data)
    else:
        print("No tasks found..")
        print("Please add new task and continue...")
        with open(task_file_path, "w") as file:
            current_user_tasks = {}
            file.write("{}")
            file.close()

'''
Method to save tasks
'''
def save_tasks():
    global current_user_tasks
    with open(task_file_path, 'w') as file:
        ensure_ascii=False
        json.dump(current_user_tasks, file, indent=4)
        file.close()

'''
Method to add task
'''
def add_task(task_description):
    global current_user_tasks
    if current_user_tasks is None:
        load_tasks()
    task = Task(task_description)
    next_task_id = 0
    #get the last task id from the task_current_user. If the task_current_user is empty, set the last_task_id to 0
    if (current_user_tasks is None or len(current_user_tasks) == 0):
        last_task_id = 0
    else:
        last_task_id = max(current_user_tasks, key=current_user_tasks.get)
        next_task_id = int(last_task_id) + 1
    current_user_tasks[next_task_id] = json.dumps(task.__dict__)
    save_tasks()

''''
Method to view tasks
'''
def view_tasks():
    global current_user_tasks
    if current_user_tasks is None:
        load_tasks()
    if len(current_user_tasks) == 0:
        print("No tasks found")
        return
    for task_id, task in current_user_tasks.items():
        task_object = json.loads(task)
        task = Task(task_object['description'])
        print(f"{task_id} : {task_object['description']} : {task_object['status']}")

''''
Method to update tasks
'''
def update_task(task_id, status_str):
    global current_user_tasks
    if current_user_tasks is None:
        load_tasks()
    if len(current_user_tasks) == 0:
        print("No tasks found")
        return
    #upddate the status of the task
    task = json.loads(current_user_tasks[task_id])
    task['status'] = status_str
    current_user_tasks[task_id] = json.dumps(task)
    save_tasks()  

'''
Method to delete task
'''
def delete_task(task_id):
    global current_user_tasks
    if current_user_tasks is None:
        load_tasks()
    if len(current_user_tasks) == 0:
        print("No tasks found")
        return
    del current_user_tasks[task_id]
    save_tasks()