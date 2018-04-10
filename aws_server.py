#!/usr/bin/python2.7

import socket
from threading import Thread
from SocketServer import ThreadingMixIn

TCP_IP = socket.gethostbyaddr("ec2-13-250-163-187.ap-southeast-1.compute.amazonaws.com")[0]
TCP_PORT = 60001
BUFFER_SIZE = 1024

print 'TCP_IP=',TCP_IP
print 'TCP_PORT=',TCP_PORT

class ClientThread(Thread):

  def __init__(self,ip,port,sock):
    Thread.__init__(self)
    self.ip = ip
    self.port = port
    self.sock = sock
    print 'New thread started for ' + ip + ':' + str(port)

  def run(self):
    f = open('./owl.stl','rb')
    while True:
      l = f.read(BUFFER_SIZE)
      while(l):
        self.sock.send(l)
        l = f.read(BUFFER_SIZE)
      if not l:
        f.close()
        self.sock.close()
        print 'File transfer job for ' + ip + ':' + str(port) + ' done.'
        break

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
  tcpsock.listen(5)
  print 'Listening ...'
  (conn, (ip, port)) = tcpsock.accept()
  print 'Connected to ', (ip,port)
  newthread = ClientThread(ip,port,conn)
  newthread.start()
  threads.append(newthread)

for t in threads:
  t.join()
