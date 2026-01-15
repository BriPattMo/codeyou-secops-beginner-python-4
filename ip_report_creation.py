with open("ips.txt") as f:
    ip_addresses = [line.strip() for line in f if line.strip()]

internal_ips = []
external_ips = []

for ip in ip_addresses:
    if ip.startswith(("192.168.", "10.")):
        internal_ips.append(ip)
    else:
        external_ips.append(ip)

with open("internal_ips.txt", "w") as out:
    out.write("Internal IP Report\n")
    out.write("--------------------------------------\n")
    out.write(f"Total Internal IPs: {len(internal_ips)}\n\n")
    for ip in internal_ips:
        out.write(ip + "\n")

with open("external_ips.txt", "w") as out:
    out.write("External IP Report\n")
    out.write("--------------------------------------\n")
    out.write(f"Total External IPs: {len(external_ips)}\n\n")
    for ip in external_ips:
        out.write(ip + "\n")