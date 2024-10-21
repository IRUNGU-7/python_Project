import socket
import time

def scanner(ip,port):
	try:
		sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.5)
		sock.connect((ip,port))
		print(f"[!]port {port} is open")
	execpt:
		none
		
def main():
	start_time=time.time()
	ip_addr=input("[~] what is target ip address:")
	port+inupt("[~] enter port number range (separated by comma ','):")
	port_range=port.split(',')
	print(f"[~] scanning {ip,addr}.")
	
	for i in range(int(port_range[0]), int(port_range[1])):
			scanner(ip_addr,i)
			
	end_time=time.time()
	print(f"scanned {port_range[1]} ports in {end_time - start_time} seconds.")
if _name_ == "-main_"
main()
