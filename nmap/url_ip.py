import socket
import nmap
import ipaddress
import re
#-------------------format for ipv4 address/port-------------------
ip_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_entered_pattern = re.compile("([0-9]+)-([0-9]+)")
min_port = 0
max_port = 65535
#------------------------------------------------------------------

nm=nmap.PortScanner()
#while True:
ip_entered = input("[IP/URL] Enter URL/IP address : ")
    #port_entered = input("[PORT] Enter range port to scan (ex: 80-443) ")
if ip_pattern.search(ip_entered): 
 print("[+] Scanning ",ip_entered)
    
else:
 ip_add=socket.gethostbyname(ip_entered)
 print("[+] Scanning ",ip_entered,"(",ip_add,")")
 ip_entered=ip_add

def scanhosts():
	scan_range = nm.scan(hosts=ip_entered)
	print(scan_range['scan'])
	return() 
    
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

#x=scan_range['scan']
#output=json.loads(x)
#print (x)
