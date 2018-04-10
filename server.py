#!/usr/bin/python2.7

import socket
import sys

s = socket.socket()
host = socket.gethostname()
port = 12345

if len(sys.argv):
  for each in sys.argv[1:]:
    if '=' in each:
      argument = each.split('=')
      if argument[0] == '--port':
        port = int(argument[1])

print 'host : ', host
print 'port : ', port

s.bind((host,port))

incoming = 0

s.listen(5)
while True:
  c, addr = s.accept()
  print 'Got connection from', addr, '.'
  text =  c.recv(1024)
  print 'Received message : ', text
  with open('./uploads/file_'+str(incoming)+'.txt','w') as file:
    file.write(text+'\n')
  file.close()
  c.send('Thanks for connecting.')
  c.close()
  print 'Connection ended.'
  incoming += 1

s.close()
