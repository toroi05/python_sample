import portscan

targets_ip = input('[+] * Enter target scan for vulnerable open ports * : ')
port_number = int(input ('[+] * Amount of port to scan * : '))
#vul_file = input ('[+] Enter path to file with vulnerable software : ')
print('\n')

target = portscan.PortScan(targets_ip, port_number) #call portscan.py
target.scan()


vulportcount=len(target.banners)

for x in range (vulportcount):
	print ('[!!] VULNURABLE BANNER: "' + target.banners[x] + '" ON PORT: ' + str(target.open_ports[x]) )
