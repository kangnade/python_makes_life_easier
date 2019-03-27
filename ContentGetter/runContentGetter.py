"""
The file that runs the program
"""

import os
import pathlib
import sys
from content_key_writer import content_key_writer, del_account
from get_content import get_content

#def get_path():
    #PATH = 'C:/Users/nade/Desktop/randomprojects'
    #return PATH

def get_path():
     while True:
         file_path = input("Please enter file path (up to folder level); q to quit:> ") 
         if os.path.isdir(file_path):
             return file_path
         elif file_path.lower() == 'q':
             sys.exit()
         else:
             print("The path you entered is invalid.")
             continue

def get_file_name():
    file_name = input("Please enter the file name (e.g. xyz.json): ") 
    return file_name

def get_account():
    account_name = input("Please enter the account name:> ")
    return account_name

def enter_content():
    content = input("Please enter the content:> ")
    return content

def main():
    print("""
    Welcome, you are using the ContentGetter. Though ContentGetter
    uses Python Cryptography to encrypt your saved information, please
    do not use it to store important passwords on sites such as Bank 
    , Amazon, Facebook, or Instagram where Hackers could be a potential
    threat.

    It's fine to use it to store information with your CV, if you are
    copying and pasting all the time to fill out only application, this
    could make your life easier!
    """)

    print("Press Y/y to continue; press any key to quit")
    user_input = input("Are you going to use the ContentGetter?> ")
    if user_input.lower() == 'y':
        # continue
        path = get_path()
        file_name = get_file_name()
        while True:
            user_want = input("Would you like to (add), (get), (del) content?> (Press any key to quit):> ")
            if user_want.lower() == "add":
                # add account and its content to the file
                account = get_account()
                content = enter_content()
                content_key_writer(path, file_name, account, content)

            elif user_want.lower() == "get":
                # get the content from the account in the file
                account = get_account()
                get_content(path, file_name, account)
            elif user_want.lower() == 'del':
                # delete the account from file
                account = get_account()
                del_account(path, file_name, account)
            else:
                break

    else:
        print("Thank you for using ContentGetter.")
    
    
        
if __name__ == '__main__':
    main()
