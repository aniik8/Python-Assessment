"""
This module provides a function to handle and calls all the necessary operations \
    for a TO-DO interface.
"""
#from modules.welcome import print_welcome_message
from modules.manager import print_manager_header, print_commands
from modules.status import show_status
from modules.tasks import add_task, show_remaining, delete_task, completed_task

def main():
    """
    Main function to execute the TO-DO interface.
    """
#    print_welcome_message()
    print_manager_header()
    print_commands()

    start = 1

    while start:
        print()
        task = input()

        if task == "help":
            print_commands()

        elif task == "report":
            show_status()

        elif task[0:4] == "add ":
            add_task(task)

        elif task == "ls":
            show_remaining()

        elif task[0:5] == "done ":
            completed_task(task[5:])

        elif task[0:4] == "del ":
            result = delete_task(task[4:])
            print(result[0])

        elif task == "close":
            print('Are you sure you want to close the application?\
                  \nPress "enter" to confirm\nPress "any key" to decline')
            decide = input()
            if len(decide) > 0:
                pass
            else:
                start = 0

        else:
            print("** Not a valid command **")

if __name__ == "__main__":
    main()
