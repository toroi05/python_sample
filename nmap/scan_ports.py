import socket
import nmap
import re
#-------------------format for ipv4 address/port-------------------
ip_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
#------------------------------------------------------------------
nm=nmap.PortScanner()
ip_entered = input("[IP/URL] Enter URL/IP address : ")
if ip_pattern.search(ip_entered): 
 print("[+] Scanning ",ip_entered)    
else:
 ip_add=socket.gethostbyname(ip_entered)
 print("[+] Scanning ",ip_entered,"(",ip_add,")")
 ip_entered=ip_add

    
def scanhosts_output():
	scan_range = nm.scan(hosts=ip_entered)
	nm.all_hosts()
	for host in nm.all_hosts():
		print ("Host: %s(%s)" %(host, nm[host].hostname()))
		print("[+]Open TCP Ports :")
		print("%s" % (nm[host].all_tcp()))
		print("[+]Open UDP Ports :")
		print("%s" % (nm[host].all_udp()))
	return()

scanhosts_output()
