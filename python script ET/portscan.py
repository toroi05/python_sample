import socket
from IPy import IP


def scan(target):    #function main utk scan
	converted_ip = check_ip(target)
	print('\n' + '[Scanning target]--> ' + str(target))
	for port in range (1,100): #boleh tukar nak port berapa 
		scan_port(converted_ip, port)

def check_ip(ip):
	try:
		IP(ip)
		return(ip)
	except ValueError:
		return socket.gethostbyname(ip) #tukar domain name ke ipaddress

def get_banner(s):      # utk banner port yg terbukak
	return s.recv(1024) # nombor just utk byte. banner tak banyak byte pun so pakai 1024 pun dah cukup


def scan_port(ipaddress,port):
	try:                       
		sock = socket.socket()   #kalau port open dia akan masuk sini
		sock.settimeout(0.5)
		sock.connect((ipaddress, port))
		try:
			banner = get_banner(sock)
			print('[+] Open Port ' + str(port) + ':' + str(banner.decode().strip('\n'))) #kalau ada banner
		except:
			print('[+] Open Port ' + str(port)) #kalau takda banner
	except:
		pass #kalau port close, akan pass



if __name__ == '__main__': #<-----kalau call dari program lain
	targets = input('[+] Domain/IP to scan : (split multiple target with , ) :')
	if ',' in targets:
		for ip_add in targets.split(','):
			scan(ip_add.strip(' ')) #kalau ada multiple (jumpa ,) 
	else:
		scan(targets) #kalau single ip/domain



