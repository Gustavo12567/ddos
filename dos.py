import socket
import os
import sys
count = 0
def init(ip,port,main):
	cliente = socket.socket(socke.AF_INET, socket.SOCK_STREAM)
	cliente.settimeout(0.03)
	code = cliente.connect_ex((ip, int(port)))
	if code == 0:
		print ('realizando ataque')
		print ('IP: /s , PORT: /s', ip,port)
	else:
			print('servidor indisponivel ou porta fechada! /n')
if len(sys.argv) < 3:
	print ('\n\n')
	print ('modo de uso')
	print('EXE: root@localhost -# python DoS.py 192.168.1.1  80')
	print('\n\n')
	sys.exit(0)
else:
	ip = sys.argv[1]
	port = sys.argv[2]
	quantia = int(sys.argv [3])
	while count < quantia:
		count += 1
		init = (ip,port,main)
		print('DoS parado')