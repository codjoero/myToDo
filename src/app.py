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
    combo, then creates a new account otherwise
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
    
    #ENTRY INTO PROGRAM
    user = input("Welcome! Have an Account? Y or N: ")
    count = 1
    while True:
        if count == 3:
            raise SystemExit('Too many wrong inputs! Exiting...')

        elif user.upper() == 'Y':
            user_check()
            #more code
            break
        elif user.upper() == 'N':
            print("------------------------")
            print("Let's create an account.")
            print("------------------------")
            input_check()
            add_account(userName, password)
            break
        else:
            user = input("I didn't get you...: ")
            count += 1
        
    """
    Enter User's profile
    """

    display = ["Create Task", "Delete Task", "Delete all Tasks", "Mark a task finished"]

    print("Select Option:")
    for i in range(4):
        indent = str(i + 1)
        print("%s. %s" % (indent.rjust(4), display[i]))

    """
    Making a selection
    """
    func_select = {
        1 :create_task, 
        2 :delete_task, 
        3 :delete_all_tasks, 
        4 :mark_as_finished
        }
    count = 0
    while True:
        if count == 3:
            raise SystemExit('Too many wrong inputs! Exiting...')
        else:
            selection = input("selection: ")
            if selection.isdigit() and 0 < selection > 5:
                func_select[selection]()
                break
            else:
                print("Make a selection 1 -- 4!")
                count += 1

    

  