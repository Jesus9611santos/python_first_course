# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

 

# Example 1:

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:

# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"

def defang_ip_addr(address):
    ip = ""
    for i in address:
        if i == '.':
            ip += '[.]'
        else:
            ip += i

    return ip

address = "1.1.1.1"
address = "255.100.50.0"
print(defang_ip_addr(address))