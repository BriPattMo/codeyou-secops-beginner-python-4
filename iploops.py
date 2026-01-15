ip_addresses = [
    "192.168.1.25",
    "10.0.0.8",
    "172.16.5.14",
    "8.8.8.8",
    "172.15.3.2"
]

internal_ips = 0
external_ips = 0

'''
for ip in ip_addresses:
    print(ip)
'''

'''
for ip in ip_addresses:
    if ip.startswith("192.168.") or ip.startswith("10."):
        print(f"{ip} is an internal address.")
    else:
        print(f"{ip} is an external address.")
'''

'''
for ip in ip_addresses:
    if ip.startswith("192.168."):
        zone = "Private (Class C)"
    elif ip.startswith("10."):
        zone = "Private (Class A)"
    elif ip.startswith("172.16.") or ip.startswith("172.17.") or ip.startswith("172.31."):
        zone = "Private (Class B)"
    else:
        zone = "Public"

    print(f"{ip} → {zone}")
'''

index = 0
while index < len(ip_addresses):
    ip = ip_addresses[index]

    if ip.startswith(("192.168.", "10.")):
        internal_ips += 1
        print(f"{ip} is internal.")
         
    else:
        external_ips +=1
        print(f"{ip} is external.")

    index += 1

print(f"Internal IPs = {internal_ips}")
print(f"External IPs = {external_ips}") 