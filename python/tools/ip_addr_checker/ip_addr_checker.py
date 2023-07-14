#script to check for valid ips in a log file
import ipaddress

def validate_ip_addresses(ip_list):
    valid_ips = []
    for ip in ip_list:
        try:
            ipaddress.ip_address(ip)
            valid_ips.append(ip)
        except ValueError:
            pass
    return valid_ips

#file location
log_file = 'var/log/file.log'

#read IP addresses from the log file
with open(log_file, 'r') as file:
    ip_list = file.read().splitlines()

#validate the IP addresses
valid_ips = validate_ip_addresses(ip_list)

print("Valid IP addresses:\n{valid_ips}")