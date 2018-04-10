#!/usr/bin/python2.7

import socket
import sys

s = socket.socket()
host = socket.gethostname()
port = 12345
text = 'hello'
if len(sys.argv):
  for each in sys.argv[1:]:
    if '=' in each:
      argument = each.split('=')
      if argument[0] == '--port':
        port = int(argument[1])
    else:
      text = each

s.connect((host,port))
s.send(text)
print s.recv(1024)
s.close()
