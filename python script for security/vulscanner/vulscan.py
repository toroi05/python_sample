import portscan

targets_ip = input('[+] * Enter target scan for vulnerable open ports * : ')
port_number = int(input ('[+] * Amount of port to scan * : '))
vul_file = input ('[+] Enter path to file with vulnerable software : ')
print('\n')

target = portscan.PortScan(targets_ip, port_number) #call portscan.py
target.scan()

#with open(vul_file, 'r') as file:
	count = 0
	for banner in target.banners:
		file.seek(0)
		for line in file.readlines():
			if line.strip() in banner:
				print ('[!!] VULNURABLE BANNER: "' + banner + '" ON PORT: ' + str(target.open_ports[count]) )
