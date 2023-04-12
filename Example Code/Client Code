# Clientcode
from socket import *

# Name and port number of the server to
# which want to connect .
serverName = "ecs.fullerton.edu"
server_Port = 12000

# Create a socket
client_Socket = socket(AF_INET, SOCK_STREAM)

# Connect to the server
client_Socket.connect((serverName, server_Port))

# A string we want to send to the server
data = "Hello world! This is a very long string."

# Send that string!
client_Socket.send(data)

# Close the socket
client_Socket.close
