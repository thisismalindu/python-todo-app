# python-todo-app

> A simple CLI based Todo app made in Python

This is my first python program. I want to take on the challenge to create something like this in python based on my knowledge in other programming languages like C++ and JavaScript.
Therefore, this app is a pretty simple app without much going on.

## Features

1. View Todo List
2. Add New Items
3. Remove Items
4. Clear List
5. Saves list to file (persistent)
6. Backup System

## How to run

To run this app, you need Python installed. If you don't have it installed already, you can download it from the official [Python website](https://www.python.org/downloads/).
After that,

1. **Install Colorama**:
   This application requires the `colorama` library. So first you need to install it.
   ```
   pip install colorama
   ```
2. **Clone the repository:**

   ```
   git clone https://github.com/thisismalindu/python-todo-app.git
   ```

3. **Navigate to the project directory:**

   ```
   cd python-todo-app
   ```

4. **Run the application:**
   ```
   python todo.py
   ```

The application will start, and you can follow the on-screen menu to perform various tasks with your todo list.

The code is well organized and should be easy to read through and understand.

## Backup Functionality

This app includes a backup system to make sure you don't accidently remove an item or delete your entire todo list. When you remove a todo item or clear your todo list, the app will create a backup with the current todo list. You can later restore this backup using the **Restore Backup** functionality.

**NOTE:** The backup system is not like a version control system, atleast at the moment. So whenever you remove an item or clear the todo list, the backup file is overwritten. So if you want to keep backups of certain lists, you will have to either have copies of the `todo_file.conf` or `todo_file_backup.conf` files or just copy the list from the console and save it somewhere. Version control is a feature we are hoping to integrate in the future.

## Screenshots
| ![When First Run python-todo-app](https://github.com/thisismalindu/python-todo-app/assets/39488765/4c9c38e4-261f-42f4-bc82-ae459eb417ea) | ![Add new Item](https://github.com/thisismalindu/python-todo-app/assets/39488765/2b3a63a2-505d-4131-ac47-b29656ff7af3) |
| --- | --- |
| ![Remove Item](https://github.com/thisismalindu/python-todo-app/assets/39488765/5407f6be-f968-4947-8cb1-5c3dc83bb344) | ![Clear List](https://github.com/thisismalindu/python-todo-app/assets/39488765/ad416e2c-7151-41f0-9429-2bc3bd13ddf6) |
