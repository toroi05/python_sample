import socket
import nmap
import ipaddress
import re
#-------------------format for ipv4 address/port-------------------------
ip_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_entered_pattern = re.compile("([0-9]+)-([0-9]+)")
min_port = 0
max_port = 65535
#------------------------------------------------------------------

print
while True:
    ip_entered = input("[IP/URL] Enter URL/IP address : ")
    port_entered = input("[PORT] Enter range port to scan (ex: 80-443) ")
    if ip_pattern.search(ip_entered): 
        print("[+] Scanning ",ip_entered)
        break
    else:
    	url=socket.gethostbyname(ip_entered)
    	print("[+] Scanning ",ip_entered,"(",url,")")
    	break

port_entered_valid = port_entered_pattern.search(port_entered.replace(" ",""))
if port_entered_valid:
        port_min = int(port_entered_valid.group(1))
        port_max = int(port_entered_valid.group(2))
        
        
x = nmap.PortScanner()
for port in range(min_port, max_port + 1):
    try:
        result = x.scan(ip_add_entered, str(port))
        port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
        print(f"Port {port} is {port_status}")
    except:
        print(f"Cannot scan port {port}.")