#!/usr/bin/python
import psutil
import pickle
import struct
import socket
import calendar
import time
#Author: Sudi
#this script is used to send data to graphite server in pickled format
#-=-=-=-=-=-=-=-=-=-=-=-

graphite_server = ""
carbon_pickle_port = 2004

def create_tuple(prefix,srv,percent):
  now = int(time.time())
  tuples = ([])
  path = prefix+'.'+srv+'.'+'percent'
  return(path,( now,(percent)))


def send_to_graphite(sock,tuples):
  payload = pickle.dumps(tuples,2)
#  print 'pickled data: ',payload
  size = struct.pack('L',len(payload))
#  print 'size:',size
  msg = size + payload
  print 'sending metrics to graphite..'
  sock.sendall(msg)
#  print 'DATA: ',tuples

def initialize():
  print 'connecting graphite server...'
  sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  sock.connect((graphite_server,carbon_pickle_port))
  return sock

def main():
  print 'here we go !!!'
  host = socket.gethostname().split('.')[0]
  tuples = ([])
  for i in psutil.cpu_percent(interval=1,percpu=True):
    tuples.append(create_tuple("myserver.System.CPU_CORE",host,i))
  sock = initialize()
  send_to_graphite(sock,tuples)
  sock.close()
  print 'bye bye'
if __name__ == '__main__':
  main()
