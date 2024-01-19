"""
This module provides utility functions for working with tasks in a TO-DO application.

Functions:
- add_task(task): Add a new task to the TO-DO list.
- show_remaining(): Display the remaining tasks in the TO-DO list.
- delete_task(task): Delete a task from the TO-DO list.
- completed_task(task): Mark a task as completed in the TO-DO list.
"""
REMAINING_FILE_PATH = "/home/unthinkable-lap/Documents/python-assignment2/data/remaining.txt"
COMPLETED_FILE_PATH = "/home/unthinkable-lap/Documents/python-assignment2/data/completed.txt"
def add_task(task):
    """
    Add a new task to the TO-DO list.
    """
    added_task = task[4:]
    adding_file = open(REMAINING_FILE_PATH
                       , "a", encoding="utf-8")
    adding_file.write(added_task + "\n")
    adding_file.close()
    print("Added todo: " + added_task)

def show_remaining():
    """
    Show the remaining tasks in the TO-DO list.
    """
    remaining_file = open(REMAINING_FILE_PATH, "r", encoding="utf-8")
    tasks = remaining_file.readlines()
    for i in range(len(tasks) - 1, -1, -1):
        print("[" + str(i + 1) + "] " + tasks[i])
    remaining_file.close()

def delete_task(deleted_task):
    """
    Delete a task from the TO-DO list.
    """
    message = "check"
    take = 'nothing'

    try:
        item = int(deleted_task)
    except NameError:
        message = "** Not a valid command **"

    if message[0] == '*':
        pass
    else:
        remaining_file = open(REMAINING_FILE_PATH
                              , "r", encoding="utf-8")
        tasks = remaining_file.readlines()

        try:
            take = tasks.pop(item - 1)
            remaining_file.close()
            remaining_file2 = open(REMAINING_FILE_PATH
                , "w", encoding="utf-8")
            for task in tasks:
                remaining_file2.write(task)
            remaining_file2.close()
            message = "Deleted todo #" + deleted_task
        except IndexError:
            message = "Error: todo #" + deleted_task + " does not exist. Nothing deleted."
            remaining_file.close()

    return [message, take]

def completed_task(complete_task):
    """
    Mark a task as completed in the TO-DO list.
    """
    completed_tasks = delete_task(complete_task)
    if completed_tasks[0][0] == 'E':
        message = "Error: todo #" + complete_task + " does not exist."
    elif completed_tasks[0][0] == '*':
        message = completed_tasks[0]

    else:
        completed_file = open(COMPLETED_FILE_PATH
                              , "a", encoding="utf-8")
        completed_file.write(completed_tasks[1])
        completed_file.close()

        message = "Marked todo #" + complete_task + " as done"

    print(message)
