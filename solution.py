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
  
  # connect the client 
  serverSocket.connect(("localhost", port))  
 
  # send some data 
  request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host"
  client.send(request.encode())  

  # receive some data 
  response = client.recv(4096)  
  http_response = repr(response)
  http_response_len = len(http_response)
  
  #Fill in end

  while True:
    #Establish the connection
    #print('Ready to serve...')
    connectionSocket, addr = #Fill in start      #Fill in end
    try:

      try:
        message = #Fill in start    #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = #Fill in start     #Fill in end
        
        #Send one HTTP header line into socket.
        #Fill in start

        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        #Fill in start

        #Fill in end


        #Close client socket
        #Fill in start

        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
