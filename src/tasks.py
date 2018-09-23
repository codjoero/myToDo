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
    print("%s added to List" %(task))
    print("=====================")

# Write a function deletes a task
def delete_task(task):
    """
    Removes the specified task from the todo_list
    """
    todo_list.remove(task)
    print("%s removed from List" %(task))
    print("=====================")

# Write a function that marks a task finished
def mark_as_finished(task):
    """
    Append the string label '[finished]' at the end of the task 
    if it does not already have the label appended.
    It should remain in the todo_list
    """
    l = []
    l.append(task)
    
    if '[finished]' in l:
        print("Task already marked finished!")
    else:
        l.append('[finished]')
        new_word = ''.join(l)
    
    todo_list[todo_list.index(task)] = new_word
    print("%s marked as finished" % task)
    print("=====================")
    
# Write a function deletes all tasks
def delete_all_tasks():
    """
    Empty the the todo_lsit
    """
    todo_list.clear()
    print("All Tasks Deleted!")
    print("=====================")
    