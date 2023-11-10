import os
import time
from colorama import init, Fore, Back, Style
init(autoreset=True)


# Init todo
TODO_FILE_PATH = os.path.expanduser('~/python-todo-app/todo_file.conf')
TODO_FILE_PATH_BACKUP = os.path.expanduser('~/python-todo-app/todo_file_backup.conf')

try:
    os.mkdir(os.path.expanduser('~/python-todo-app/'))
except FileExistsError:
    pass
open(TODO_FILE_PATH,'a')

todo_list = []

def todo_backup():
    todo_file_backup = open(TODO_FILE_PATH_BACKUP,'w')
    todo_string = ""
    for todo_item in todo_list:
        todo_item += '\n'
        todo_string += todo_item
    todo_file_backup.write(todo_string)


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
    print(Style.BRIGHT+ Back.LIGHTYELLOW_EX + Style.NORMAL+ Fore.BLACK + 'Todo List\n')
    for item in todo_list:
        print(str(todo_list.index(item)+1) +". " + item)
    print()    

def remove_todo():
    clear_screen()
    printTodo()
    index = input(Style.BRIGHT + Fore.RED+ "Which element do you want to remove ('/c' for cancel)? "+Style.RESET_ALL)
    if index.lower()=="/c":
        return
    try:
        index = int(index)
        if 1 <= index <= len(todo_list):
            del todo_list[index - 1]
            write_todo()
            print(Style.BRIGHT + Fore.GREEN+'Item Removed!')
            time.sleep(1)
        else:
            print(Style.BRIGHT + Fore.RED+'Invalid index. Please try again.')
            time.sleep(1)
            remove_todo()
    except ValueError:
        print(Style.BRIGHT + Fore.RED+'Invalid input. Please enter a valid index.')
        time.sleep(1)
        remove_todo()

def clear_todo():
    clear_screen()
    printTodo()
    user_input = input(Style.BRIGHT + Fore.RED + """
This action is irreversible.
Are you sure you want to clear the Todo List (Y/n)? """ + Style.RESET_ALL).lower()
    if user_input=="n":
        return
    elif user_input == "y" or user_input=="":
        todo_backup()
        todo_list.clear()
        write_todo()
        print(Style.BRIGHT + Fore.GREEN+'Todo List Cleared')
        time.sleep(1)
    else:
        print(Style.BRIGHT + Fore.RED+'Invalid input. Please enter a valid index.')
        time.sleep(1)
        clear_todo()


def add_todo():
    item = input(Style.BRIGHT+ Fore.LIGHTYELLOW_EX + "Enter a todo item ('/c' for cancel): " + Style.RESET_ALL)
    if item.lower()=="/c":
        return
    todo_list.append(item)
    write_todo()
    print(Style.BRIGHT + Fore.GREEN+'Item Added!')
    time.sleep(1)

def main_menu():
    print(Style.BRIGHT+ Fore.CYAN + 'What do you want to do?')
    return int(input('''
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
        case 1:
            pass
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
