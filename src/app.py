# ---- app.py ----
# This file contains the entry point to your tasks
# and the logic to manage it

from tasks import todo_list, create_task, delete_task, delete_all_tasks, mark_as_finished  # import other functions as well
from accounts import add_account, login # import the function as well


if __name__ == "__main__":
    """
    Allow a person to input a name and a password
    """
    userName = ''
    password = ''

    """
    Checks for string input
    """        
    def input_check():
        count = 0
        while True:
            if count == 3:
                raise SystemExit('Too many wrong inputs! Exiting...')
            else:
                userName = input("Username: ") 
                password = input("Password: ")
                #credentials = [userName, password]
            
                if userName.isalpha():
                    userName.capitalize
                    break
                else:
                    print("Username should only be a string")
                    count += 1

    """
    Gives user 3 chances to input the right username-password
    then creates a new account otherwise
    """
    def user_check():
        count = 1
        while True:
            input_check()
            if count == 3:
                print("")
                print("+++++++++++++++++++++++++++++++++++")
                print("You don't seem to have an account!")
                print("A new one has been created for you.")
                print("Welcome!")
                print("+++++++++++++++++++++++++++++++++++")
                print("")
                add_account(userName, password)
                break
            elif login(userName, password):
                break
            else:
                print("Wrong Username or Password!")
                count += 1
    """
    Local task functions:
    """
    def create_local_task():
        print("--------------------")
        print("Let's Create a Task.")
        print("--------------------")
        task = str(input("Enter Task name: "))
        create_task(task)

    def delete_local_task():
        if not todo_list:
            print("You don't have any Task in your List!")
        else:
            print("-----------------------")
            print("You're Deleting a Task.")
            print("-----------------------")
            print("Select Option:")
            for index, item in enumerate(todo_list):
                indent = str(index + 1)
                print("%s. %s" % (indent.rjust(4), item))
            count = 0
            while True:
                if count == 3:
                    raise SystemExit('Too many wrong inputs! Exiting...')
                else:
                    try:
                        task = int(input("Enter Task Number: "))
                        if  0 < task <= len(todo_list):
                            delete_task(todo_list[task - 1])
                            break
                        else:
                            print("Select the right Task Number!")
                    except ValueError:
                        print("Oops! Select the right Task Number!")                
                count += 1
    def del_all_local_task():
        if not todo_list:
            print("You don't have any Task in your List!")
        else:
            count = 0
            while True:
                if count == 3:
                    raise SystemExit('Too many wrong inputs! Exiting...')
                else:
                    confirm = input("Are you sure? Y or N: ")
                    if confirm.upper() == 'Y':
                        delete_all_tasks()
                        break
                    elif confirm.upper() == 'N':
                        break
                    else:
                        print("Choose Y or N!")
                        count += 1
    
    def mark_local_finished():
        if not todo_list:
            print("You don't have any Task in your List!")
        else:
            print("------------------------------------")
            print("You're Marking a task as [Finished].")
            print("------------------------------------")
            print("Select Option:")
            for index, item in enumerate(todo_list):
                indent = str(index + 1)
                print("%s. %s" % (indent.rjust(4), item))
            count = 0
            while True:
                if count == 3:
                    raise SystemExit('Too many wrong inputs! Exiting...')
                else:
                    try:
                        task = int(input("Enter Task Number: "))
                        if  0 < task <= len(todo_list):
                            mark_as_finished(todo_list[task - 1])
                            break
                        else:
                            print("Select the right Task Number!")
                    except ValueError:
                        print("Oops! Select the right Task Number!")                
                count += 1
    
    """
    Enter User's profile
    """
    def user_profile():
        display = ["Create Task", "Delete Task", "Delete all Tasks", "Mark a task finished"]
        print()
        print("==============")
        print("Select Option:")
        for i in range(4):
            indent = str(i + 1)
            print("%s. %s" % (indent.rjust(4), display[i]))

        """
        Making a selection
        """
        func_local = {
            1 :create_local_task, 
            2 :delete_local_task, 
            3 :del_all_local_task, 
            4 :mark_local_finished
        }
        count = 0
        while True:
            if count == 3:
                raise SystemExit('Too many wrong inputs! Exiting...')
            else:
                try:
                    selection = int(input("selection: "))
                    if  0 < selection < 5:
                        func_local[selection]()
                        user_profile()
                        break
                    else:
                        print("Make a selection 1 -- 4!")
                except ValueError:
                    print("Oops! Enter a number btn 1 and 4!")
                count += 1


    #ENTRY INTO PROGRAM
    user = input("Welcome! Have an Account? Y or N: ")
    count = 1
    while True:
        if count == 3:
            raise SystemExit('Too many wrong inputs! Exiting...')

        elif user.upper() == 'Y':
            user_check()
            user_profile()
            break
        elif user.upper() == 'N':
            print("------------------------")
            print("Let's create an account.")
            print("------------------------")
            input_check()
            add_account(userName, password)
            user_profile()
            break
        else:
            user = input("I didn't get you...: ")
            count += 1
        