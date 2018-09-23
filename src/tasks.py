# --- tasks.py ---
# This file contains code that manages your todo_list

todo_list = []

# Write a function creates a task

def create_task(task):
    """
    Adds the task (string value) to todo_list
    """
    task = str(task)
    todo_list.append(task)

# Write a function deletes a task


def delete_task(task):
    """
    Removes the specified task from the todo_list
    """
    todo_list.remove(task)

# Write a function that marks a task finished


def mark_as_finished(task):
    """
    Append the string label '[finished]' at the end of the task 
    if it does not already have the label appended.
    It should remain in the todo_list
    """
    l = []
    l.append(task)
    if '[finished]' not in l:
        l.append('[finished]')
        new_word = ''.join(l)
        return new_word

# Write a function deletes all tasks


def delete_all_tasks():
    """
    Empty the the todo_lsit
    """
    todo_list.clear()
    