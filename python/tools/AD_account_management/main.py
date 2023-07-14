#script to create new AD user account.
#the script will prompt for creds, do not hard code them in code.
from pyad import *
from pyad.adquery import ADQuery

#set up a connection to the AD server

pyad.set_defaults(ldap_server=input("enter ldap server address: "))

#bind to the AD server using appropriate credentials
pyad.aduser.set_defaults(username=input("enter admin username: "), password=input("enter pwd: "))

#get user inputs
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