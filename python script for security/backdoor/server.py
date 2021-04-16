import socket

def target_communication(): 
	message = target.recv(1024)
	print(message.decode())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 5555))
print('Listening incoming connection')
sock.listen(5)
target, ip = sock.accept()
print ('Target connected from '+ str(ip))


target_communication()
