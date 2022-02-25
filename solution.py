from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # Fill in start
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFrom = "MAIL FROM: <brendanlin7@gmail.com> \r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print("After MAIL FROM command: " + recv2)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptTo = "RCPT TO: <brendanlin7@gmail.com> \r\n"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print("After RCPT TO command: " + recv3)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print("After DATA command: " + recv4)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    subject = "Subject: SMTP mail client testing \r\n\r\n"
    clientSocket.send(subject.encode())
    clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    #print("Response after sending message body:" + recv5)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in
    clientSocket.send(".\r\n".encode())  # sends period, then blank line
    recv6 = clientSocket.recv(1024).decode()  # amount of data to be sent
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    clientSocket.send("QUIT\r\n".encode())
    recv7 = clientSocket.recv(1024).decode()
    #print(message)
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')