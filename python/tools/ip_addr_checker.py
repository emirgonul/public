import ipaddress

def validate_ip_addresses(ip_list):
    valid_ips = []
    for ip in ip_list:
        try:
            ipaddress.IPv4Address(ip)
            valid_ips.append(ip)
        except ipaddress.AddressValueError:
            pass
    return valid_ips

# Example usage
ip_list = ['192.168.0.1', '10.0.0.256', '172.16.0.1', '2001:db8:85a3::8a2e:370:7334', 'not_an_ip']
valid_ips = validate_ip_addresses(ip_list)
print(valid_ips)