"""
This module provides a function to show statistics for a TO-DO interface.
"""
def show_status():
    """
    Show statistics for the TO-DO interface.
    """
    remaining_file = open("/home/unthinkable-lap/Documents/python-assignment2/data/remaining.txt"\
                          , "r", encoding="utf-8")
    completed_file = open("/home/unthinkable-lap/Documents/python-assignment2/data/completed.txt"\
                          , "r", encoding="utf-8")
    print("Remaining Number of tasks: ", len(remaining_file.readlines()))
    print("Completed tasks: ", len(completed_file.readlines()))

    remaining_file.close()
    completed_file.close()
