# About scanning

Scanning is basically about the **technology side** of your target. First of all that we **cannot scanning random website** so for this project and your studeis we will create vulnerable VMs.

When Scanning you main goal is to look for **open ports**, for example port 80 /443 for http/https, port 53 for DNS, port 22 for SSH, por 23 for FTP, port 25 for SMTP and etc. To be exact, every machine got 65535 ports, if one is open, with one vulnerable software running on that open port then that target is vulnerable and can be exploited.

## About TCP & UDP

### TCP - Transmission Control Protocol

TCP is the most commonly used protocol on the internet, when you open a web page, post a comment you will send this packages to the webpage that will send it back to you after receive it, so it is a **three way handshake**, the steps are:

1. **SYN** Synchronized Sequence Number: The client establish a connection with the server;
2. **SYN/ACK**: The server responds to the client's request;
3. **ACK** The client acknowledges the response of server, they both establish a realiable connection with which they will start the actual data transfer.

So the client will send numereted packages and await for the server response, if the response is not what the cliente expect, it will resend the packages to ensure the server got the packages.

### UDP - User Datagram Protocol

UDP works similiar to TCP but without the error check things, this make UDP a lot faster, beucase of that UDP is usually used by brodcasts and online games.
