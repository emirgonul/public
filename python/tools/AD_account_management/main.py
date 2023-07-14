#script to create, modify user account, reset pw and unlock accounts.
#the script will prompt for creds, do not hard code them in code.
#pyad relies on LDAP protocol to communicate with AD on port 389 for LDAP communication and port 636 for LDAPS
from pyad import *
from pyad.adquery import ADQuery

#set up a connection to the AD server

pyad.set_defaults(ldap_server=input("enter ldap server address: "))

#bind to the AD server using appropriate credentials
pyad.aduser.set_defaults(username=input("enter admin username: "), password=input("enter pwd: "))

#function to create a new user
def create_user():
    #get user inputs for new user
    new_username = input("Enter the new user account name: ")
    first_name = input("Enter the user's first name: ")
    last_name = input("Enter the user's last name: ")
    email = input("Enter the user's email address: ")
    password = input("Enter the user's password: ")

    #create a new user
    new_user = pyad.aduser.ADUser.create(new_username)

    #set the required attributes for the new user
    new_user.update_attribute("givenName", first_name)
    new_user.update_attribute("sn", last_name)
    new_user.update_attribute("userPrincipalName", email)
    new_user.update_attribute("sAMAccountName", new_username)
    new_user.update_attribute("displayName", f"{first_name} {last_name}")
    new_user.update_attribute("description", "User Description")
    new_user.update_attribute("password", password)

    #save the changes
    new_user.commit_changes()

    #check if the user creation was successful
    if new_user.is_enabled():
        print("User created successfully.")
    else:
        print("Failed to create the user.")


#function to modify an existing user account
def modify_user():
    username = input("Enter the username of the account to modify: ")

    try:
        user = pyad.aduser.ADUser.from_cn(username)
    except pyad.pyadexceptions.ADPyADException:
        print(f"User '{username}' does not exist.")
        return

    #get user inputs for modifications
    first_name = input("Enter the user's new first name (leave blank to skip): ")
    last_name = input("Enter the user's new last name (leave blank to skip): ")
    email = input("Enter the user's new email address (leave blank to skip): ")

    #update attributes if provided
    if first_name:
        user.update_attribute("givenName", first_name)
    if last_name:
        user.update_attribute("sn", last_name)
    if email:
        user.update_attribute("userPrincipalName", email)

    #save the changes
    user.commit_changes()

    print(f"User '{username}' modified successfully.")


#function to reset a user's password
def reset_password():
    username = input("Enter the username of the account to reset the password: ")

    try:
        user = pyad.aduser.ADUser.from_cn(username)
    except pyad.pyadexceptions.ADPyADException:
        print(f"User '{username}' does not exist.")
        return

    password = input("Enter the new password: ")

    #reset the password
    user.set_password(password)

    print(f"Password for user '{username}' reset successfully.")


#function to unlock a user account
def unlock_account():
    username = input("Enter the username of the account to unlock: ")

    try:
        user = pyad.aduser.ADUser.from_cn(username)
    except pyad.pyadexceptions.ADPyADException:
        print(f"User '{username}' does not exist.")
        return

    #unlock the account
    user.unlock_account()

    print(f"Account for user '{username}' unlocked successfully.")


#main program loop
while True:
    print("Select an option:")
    print("1. Create a new user")
    print("2. Modify an existing user account")
    print("3. Reset a user's password")
    print("4. Unlock a user account")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        create_user()
    elif choice == "2":
        modify_user()
    elif choice == "3":
        reset_password()
    elif choice == "4":
        unlock_account()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")