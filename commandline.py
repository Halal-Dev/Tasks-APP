import sqlite3
from sqlite3 import IntegrityError
from prettytable import PrettyTable
def menu():
    print('''
     _________________________
    |   DB Tasks Editor       |
    |  Enter number to start  |
    |                         |
    | 1- Create Task          |
    | 2- Remove Task          |
    | 3- List Tasks           |
    |_________________________|
    ''')
    goto = input('Choice : ')
    if goto == '1':
        c_task()
    if goto == '2':
        d_task()
    if goto == '3':
        l_tasks()
    

def c_task():
    task_id = int(getlastid()) + 1
    task_name = input("task name : ")
    task_description = input("task description : ")
    task_done = input("is done ? (yes/no) : ")
    
    create_task(conn, (task_id, task_name, task_description, task_done))

def d_task():
    task_id = input("Task id : ")
    if task_id.isdigit():
        task_id = int(task_id)
        if checkID(task_id)
def l_tasks():
    mainTable = PrettyTable()
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    all_tasks = cur.execute("Select * from tasks").fetchall()
    mainTable.field_names = ['ID', 'Task name', 'Description', 'done']
    for task in all_tasks:
        mainTable.add_row([task[0], task[1], task[2], task[3]])
    print(mainTable)
#check if id exists
def checkID(ID):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT id FROM tasks")
    rows = cur.fetchall()
    rowlist = []
    for row in rows:
        rowlist.append(row[0])
    if ID in rowlist:
        return True
    else:
        return False
conn = sqlite3.connect('database.db')
print("Opened database successfully")
def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    cur = conn.cursor()
    if checkID(id) == True:
        try:

            sql = 'DELETE FROM tasks WHERE id=?'
            cur.execute(sql, (id,))
            conn.commit()
            print("sucessfully deleted task "+id)
        except Exception as e:
            print("An error occured" + str(e))
    else:
        print("Task not existing")

def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    try:
        
        if checkID(task[0]) == False:

            sql = ''' INSERT INTO tasks(id,title,description,done)
                    VALUES(?,?,?,?) '''
            cur = conn.cursor()
            cur.execute(sql, task)
            conn.commit()
            return cur.lastrowid
        else:
            print("ID already here")
    except Exception as e:
        print(e)

#conn.execute('CREATE TABLE tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, done TEXT)')
print("Table created successfully")
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT id FROM tasks")
    new = 5
    rows = cur.fetchall()
    rowlist = []
    for row in rows:
        rowlist.append(row[0])
    if new in rowlist:
        print("already defined task id")

def getlastid():
    cur = conn.cursor()
    cur.execute("SELECT id FROM tasks ORDER BY id DESC")
    rows = cur.fetchall()
    rowlist = []
    for row in rows:
        rowlist.append(row[0])
    return rowlist[0]
menu()
create_task(conn, (2, "new", "new", "no"))
getlastid()
conn.close()
