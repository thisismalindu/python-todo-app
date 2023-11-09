import os
import time

# Init todo
TODO_FILE_PATH = os.path.expanduser('~/todo_file.conf')
open(TODO_FILE_PATH,'a')
todo_list = []


def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def write_todo():
    todo_file = open(TODO_FILE_PATH,'w')
    todo_string = ""
    for todo_item in todo_list:
        todo_item += '\n'
        todo_string += todo_item
    todo_file.write(todo_string)

def read_todo():
    todo_file = open(TODO_FILE_PATH,'r')
    new_todo_list = todo_file.readlines()
    for todo_item in new_todo_list:
        todo_list.append(todo_item.replace('\n',''))

def printTodo():
    print('''
-----------------

Todo List
''')
    for item in todo_list:
        print(str(todo_list.index(item)+1) +". " + item)
    print('''
-----------------
''')

def remove_todo():
    clear_screen()
    printTodo()
    index = input("Which element do you want to remove ('/c' for cancel)? ")
    if index.lower()=="/c":
        return
    # index = int(index)
    # todo_list.pop(index-1) # Since 0 based index
    # write_todo()
    # print('Item Removed!')
    # time.sleep(1)
    try:
        index = int(index)
        if 1 <= index <= len(todo_list):
            del todo_list[index - 1]
            write_todo()
            print('Item Removed!')
            time.sleep(1)
        else:
            print('Invalid index. Please try again.')
            time.sleep(1)
            remove_todo()
    except ValueError:
        print('Invalid input. Please enter a valid index.')
        time.sleep(1)
        remove_todo()

def clear_todo():
    clear_screen()
    printTodo()
    user_input = input("""
This action is irreversible.
Are you sure you want to clear the Todo List (Y/n)? """).lower()
    if user_input=="n":
        return
    elif user_input == "y" or user_input=="":
        todo_list.clear()
        write_todo()
        print('Todo List Cleared')
        time.sleep(1)
    else:
        clear_todo()


def add_todo():
    item = input("Enter a todo item ('/c' for cancel): ")
    if item.lower()=="/c":
        return
    todo_list.append(item)
    write_todo()
    print('Item Added!')
    time.sleep(1)

def main_menu():
    return int(input('''
What do you want to do?
    1. View Todo List
    2. Add Todo Item
    3. Remove Todo Item
    4. Clear List
    5. Quit\n

Enter the number:'''))

read_todo()
while True:

    clear_screen()
    printTodo()

    match main_menu():
        case 2:
            add_todo()
        case 3:
            clear_screen()
            remove_todo()
        case 4:
            clear_todo()
        case 5:
            clear_screen()
            break
        case _:
            print('Invalid choice. Please select a valid option.')
            time.sleep(1)
