#!/usr/bin/python
# -*- coding: utf-8 -*-
#import conf.config as config
import socket
def SendInfo(ip):
	try:
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		#sock.connect((config.scan_service_host,config.scan_service_port))
		sock.connect(("192.168.64.131",9011))
		message=ip+";9011"
		sock.send(message.encode())
		print(sock.recv(1024))
	except Exception as e:
		print (e) 
SendInfo(ip)