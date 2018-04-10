#!/usr/bin/python2.7

import socket

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
with open('received_file','wb') as f:
  print 'Start receiving ...'
  while True:
    data = s.recv(BUFFER_SIZE)
    if not data:
      f.close()
      print 'File transfer job done.'
      break
    f.write(data)

print('Connection ended.')
s.close()
