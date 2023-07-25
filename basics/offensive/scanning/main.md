# About scanning

Scanning is basically about the **technology side** of your target. First of all that we **cannot scanning random website** so for this project and your studeis we will create vulnerable VMs.

When Scanning you main goal is to look for **open ports**, for example port 80 /443 for http/https, port 53 for DNS, port 22 for SSH, por 23 for FTP, port 25 for SMTP and etc. To be exact, every machine got 65535 ports, if one is open, with one vulnerable software running on that open port then that target is vulnerable and can be exploited.

## About TCP & UDP

### TCP - Transmission Control Protocol

TCP is the most commonly used protocol on the internet, when you open a web page, post a comment you will send the packet to the webpage that will send it back to you after receive it, so it is a **three way handshake**, the steps are:

1. **SYN** Synchronized Sequence Number: The client establish a connection with the server;
2. **SYN/ACK**: The server responds to the client's request;
3. **ACK** The client acknowledges the response of server, they both establish a realiable connection with which they will start the actual data transfer.

So the client will send numereted packets and await for the server response, if the response is not what the cliente expect, it will resend the packets to ensure the server got the packets.

UDP works similiar to TCP but without the error check things, this make UDP a lot faster, beucase of that UDP is usually used by brodcasts and online games.

## Building the vulnerable VMs

To build it I will use [Metasploitable](https://information.rapid7.com/download-metasploitable-2017.html?LS=1631875&CS=web) from rapid. Metasploitable is free to use, but we must fill a form at the end of page in order to download it.

We start the VM and use the `msfadmin:msfadmin` to login.

## ARP

ARP is a tool on kali linux to discorvering hosts on a network, arp must be run with sudo privileges always.
To a host appearo in `sudo arp -a` we must first ping it. In my case my metasploitable VM is on port .3 so i ping like `ping xxx.xxx.x.3` and after `sudo arp -a` appears both my router and my VM. To avoid this a better option for tool is **Netdiscover**

## Netdiscover

Netdiscorver also need sudo privileges to run, simply `sudo netdiscover` this will start to scanning all subnets and will find all avaliable hosts without need to ping it.

## NMAP

Unlike all the other tools that sometimes we use or sometime not **nmap** is basically a must use tool for every pentest. Nmap is a _network mapper_, it is used to discorver hosts and services in a network by sending packets and analyze responses.
Since I am running a metasploitable VM on my own network I just run `sudo netdiscover` in order to "figure" the IP of my target, then run nmap to scanning: `nmap [ip and subnet of my vm]`
Is my network, so it run real fast and show me a lot of tcp ports open. True nmap scans will take **hours** to finish!
We got some default ports like SSH, FTP, telnet, but in metasploitable we also got different services, like mysql, postgres and etc. Remember that by default nmap will scan the most commom **1000** ports, not all the 65,000.
To scan all the subnet we can specify by going to 1 to **/24** that represents that **the first three octets doesn't change**.
