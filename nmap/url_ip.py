import socket
#import nmap
import ipaddress
import re
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
while True:
    ip_entered = input("[IP/URL] Enter URL/IP address : ")
    port_entered = input("[PORT] Enter port to scan : ")
    if ip_add_pattern.search(ip_entered): 
        print("[+] Scanning ",ip_entered)
        break
    else:
    	url=socket.gethostbyname(ip_entered)
    	print("[+] Scanning ",ip_entered,"(",url,")")
    	break;


        
