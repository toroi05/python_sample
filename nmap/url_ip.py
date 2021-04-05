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
open_ports = []
print
while True:
    ip_entered = input("[IP/URL] Enter URL/IP address : ")
    port_entered = input("[PORT] Enter range port to scan (ex: 80-443) ")
    if ip_pattern.search(ip_entered): 
        print("[+] Scanning ",ip_entered)
        break
    else:
    	ip_entered=socket.gethostbyname(ip_entered)
    	print("[+] Scanning ",ip_entered,"(",url,")")
    	break
