"""
This module provides functions to print manager headers and commands for a TO-DO interface.
"""
def print_manager_header():
    """
    Print manager header for the TO-DO interface.
    """
    print("-------------------------------------------")
    print("MANAGE ALL YOUR TASKS AND BE MORE ORGANIZED")
    print("-------------------------------------------")
    print('type "help" to know the commands')

def print_commands():
    """
    Print available commands for the TO-DO interface.
    """
    print("Usage :-")
    print('add "todo item"    # Add a new todo')
    print('ls        # Show remaining todos')
    print('del "Number"    # Delete a todo')
    print('done "Number"    # Complete a todo')
    print('help        # Show commands')
    print('report        # Statistics')
    print('close         # Close the application')
