# import socket module
from socket import *
# In order to terminate the program
import sys

#socket: network node used to send and receive data across a network
def webServer(port=13331):
  #create socket; INET=IPv4 sockets, and STREAM=TCP sockets
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind(("localhost", port)) #socket is reachable by any address, hence the "", and the port-13331, as specified in the webServer function
  #Fill in start
  serverSocket.listen(1)
  # connect the client 
  # serverSocket.connect(("localhost", port))  
  
  #Fill in end

  while True:
    #Establish the connection
    #print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start      #Fill in end
    try:

      try:
        message = connectionSocket.recv(1024)   #Fill in start    #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() #Fill in start     #Fill in end
        
        #Send one HTTP header line into socket.
        #Fill in start
        okMessage = 'HTTP/1.1 200 OK \r\n'
        connectionSocket.send(okMessage.encode())
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        #Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found\n\n")
        #Fill in end


        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
