import socket
import random
import sys
from threading import Thread

N_BITS = 10	#1,000,000

def send_data (thread_name, ip_address, port):
	print "Starting " + thread_name
	while (True):
		bits = random.getrandbits(N_BITS)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(str(bits), (ip_address, int(port)))

print "Number of arguments is " + str(len(sys.argv))
print "IP address is " + str(sys.argv[1])
print "port is " + str(sys.argv[2])

IP = str(sys.argv[1])
PORT = sys.argv[2]

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