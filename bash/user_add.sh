#script to automate user creation
#in case of a successful account creation assign the user account a password as their username

#!/bin/bash

#get password and user name
PASS=$(which passwd)
ADD=$(which useradd)

for user in user{1..2..3};do
        echo "Creating user : $user"
        #ignore the output from useradd
        $ADD $user > /del/null 2>&1

        if [ $? = 0 ]
        then
                echo "==============="
                echo "The account $user created successfully"
                echo $user | $PASS --stdin $user
        else
                echo "Failed to create account $user"
        fi