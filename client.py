import socket  
import select  
import sys  
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
if len(sys.argv) != 2:  
    print ("Correct usage: script, Client name") 
    exit()  
IP_address = '127.0.0.1'
Port = 30176 
server.connect((IP_address, Port))
server.send(str(sys.argv[1])) 
c=1;
while c:  
   
    sockets_list = [sys.stdin, server]  
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])  
  
    for socks in read_sockets:  
        if socks == server:  
            message = socks.recv(2048) 
            print (message)  
        else: 
            message = sys.stdin.readline()
            if message.strip() =='exit':
                c=0
            server.send(message)  
            sys.stdout.write("You: ")  
            sys.stdout.write(message)  
            sys.stdout.flush()  
server.close()  