#!/usr/bin/python2.7

import socket
import sys

s = socket.socket()
host = socket.gethostname()
port = 12345
filename = './hello.txt'

if len(sys.argv):
  for each in sys.argv[1:]:
    if '=' in each:
      argument = each.split('=')
      if argument[0] == '--port':
        port = int(argument[1])
    else:
      filename = each

s.connect((host,port))
print 'Connected to server.'
f = open(filename,'rb')
l = f.read(1024)
part = 1
while(l):
  print 'Sending data ... (%s)' % part
  s.send(l)
  l = f.read(1024)
  part += 1
f.close()
print 'Done file transfer job.'
s.close()
