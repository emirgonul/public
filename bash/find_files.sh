#script to find files between specific ranges for specified user
#!/bin/bash
echo "Enter username: "
read username
echo "Enter file size range in KB:"
echo "from: "
read from_size
echo "to:"
read to_size
find / -type f -user $username -size +$from_size -size -$to_size -exec cp {} /tmp/ \;