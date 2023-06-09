# Server code
from socket import *

# The port on which to listen
server_Port = 12000

# Create a TCPs ocket
server_Socket = socket(AF_INET, SOCK_STREAM)
# Bind the s ocke t to the port
server_Socket.bind((' ', server_Port))

# Start listening for incoming connections
server_Socket.listen(1)
print('The server is ready to receive')

# Forever accept incoming connections
while 1:
# Accept a connection ; get client's socket
    connection_Socket, addr = server_Socket.accept()

# Receive whatever the newly connected client has to send
data = connection_Socket.recv(40)
print(data)

# Close the socket
connection_Socket.close()
