'''
print("REPORT SCRIPT STARTED\n")

ip_addresses = [
    "192.168.1.25",
    "10.0.0.8",
    "172.16.5.14",
    "8.8.8.8",
    "172.15.3.2"
]

internal_ips = []
external_ips = []

index = 0
while index < len(ip_addresses):
    ip = ip_addresses[index]

    if ip.startswith(("192.168.", "10.")):
        #internal_ips += 1
        internal_ips.append(ip)
        #print(f"{ip} is internal.")
         
    else:
        #external_ips +=1
        external_ips.append(ip)
        #print(f"{ip} is external.")

    index += 1

print("IP Classifications")
print("------------------------------------------")
print(f"Internal IPs ({len(internal_ips)}):")
print(internal_ips)
print()
print(f"External IPs ({len(external_ips)}):")
print(external_ips)
print("\nREPORT SCRIPT ENDED")
#print(f"Internal IPs = {internal_ips}")
#print(f"External IPs = {external_ips}") 
'''

#CHALLANGE 3
ip_addresses = []

#Collect input until done
while True:
    ip = input("Enter an IP (or 'done' to finish): ").strip()

    if ip.lower() == "done":
        break

    ip_addresses.append(ip)

#Classify
internal_ips = []
external_ips = []

index = 0
while index < len(ip_addresses):
    ip = ip_addresses[index]

    if ip.startswith(("192.168.", "10.")):
        internal_ips.append(ip)
    else:
        external_ips.append(ip)

    index += 1

#Report
print("REPORT SCRIPT STARTED\n")
print("IP Classifications")
print("------------------------")
print(f"Internal IPs ({len(internal_ips)}):")
print(internal_ips)
print()
print(f"External IPs ({len(external_ips)}):")
print(external_ips)
print("\nREPORT SCRIPT ENDED")



