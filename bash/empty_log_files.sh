#execute with hostname --> sudo ./empty_logs.sh <hostname>
#!/bin/bash

log_files=(
    "/var/log/messages"
    "/var/log/syslog"
    "/var/log/auth.log"
    # Add more log files as needed
)

# Function to empty log files for a specific hostname
empty_logs() {
    local hostname="$1"

    for log_file in "${log_files[@]}"; do
        if [ -f "$log_file" ]; then
            echo "Emptying $log_file for $hostname..."
            echo -n > "$log_file"
            echo "Done."
        else
            echo "Log file $log_file not found for $hostname."
        fi
    done
}

# Check if the hostname argument is provided
if [ -z "$1" ]; then
    echo "Hostname argument is missing."
    echo "Usage: ./empty_logs.sh <hostname>"
    exit 1
fi

# Call the function to empty logs for the provided hostname
empty_logs "$1"