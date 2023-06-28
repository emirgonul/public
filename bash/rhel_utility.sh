: '
#sudo ./rhel_utility.sh
RHEL utility script to get sysinfo
0. Exit 
1. Get System Information
2. Get CPU Usage
3. Get Memory Usage
4. Get Disk Space
5. Get Network Interfaces
6. Run System Update
'

#!/bin/bash

# Function to check system information
get_system_info() {
    echo "System Information:"
    echo "-------------------"
    uname -a
    cat /etc/redhat-release
    echo ""
}

# Function to check CPU usage
get_cpu_usage() {
    echo "CPU Usage:"
    echo "----------"
    mpstat
    echo ""
}

# Function to check memory usage
get_memory_usage() {
    echo "Memory Usage:"
    echo "-------------"
    free -h
    echo ""
}

# Function to check disk space
get_disk_space() {
    echo "Disk Space:"
    echo "-----------"
    df -h
    echo ""
}

# Function to check network interfaces
get_network_interfaces() {
    echo "Network Interfaces:"
    echo "-------------------"
    ip addr show
    echo ""
}

# Function to run system updates
run_system_update() {
    echo "Running System Update..."
    yum update -y
    echo "System Update Completed."
    echo ""
}

# Main script logic
while true; do
    echo "RHEL Utility Script"
    echo "-------------------"
    echo "1. Get System Information"
    echo "2. Get CPU Usage"
    echo "3. Get Memory Usage"
    echo "4. Get Disk Space"
    echo "5. Get Network Interfaces"
    echo "6. Run System Update"
    echo "0. Exit"
    echo ""
    read -p "Enter your choice (0-6): " choice

    case $choice in
        1) get_system_info ;;
        2) get_cpu_usage ;;
        3) get_memory_usage ;;
        4) get_disk_space ;;
        5) get_network_interfaces ;;
        6) run_system_update ;;
        0) exit ;;
        *) echo "Invalid choice. Please try again." ;;
    esac

    echo ""
done