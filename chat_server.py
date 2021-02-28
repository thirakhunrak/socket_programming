import socket  
import select  
import sys  
from thread import *
  

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  

IP_address = '127.0.0.1'
Port = 30176  #6131017621  -> 10176+20000 = 30176

server.bind((IP_address, Port))  

server.listen(10)  
  
dict_of_clients = dict()  
  
def clientthread(conn, addr):  
    client_name = dict_of_clients.get(conn)  
    conn.send("Welcome '"+ client_name + "' to this chatroom!")  
  
    while True:  
            try:  
                message = conn.recv(2048)  
                if message:  
  
                    print (client_name + ": " + message)  
   
                    message_to_send = client_name + ": " + message  
                    broadcast(message_to_send, conn)  
  
                else:  
                    remove(conn)  
  
            except:  
                continue
  
def broadcast(message, connection):  
    for clients in dict_of_clients:  
        if clients!=connection:  
            try:  
                clients.send(message)  
            except:  
                clients.close()  
                remove(clients)  
  
def remove(connection):  
    if connection in dict_of_clients:  
        dict_of_clients.pop(connection)  
  
while True:  
  
    conn, addr = server.accept()  
    
    temp = conn.recv(2048)
    name = str(temp)
    dict_of_clients[conn] = name
    print (name + " connected") 
  
    start_new_thread(clientthread,(conn,addr))      
  
conn.close()  
server.close()  