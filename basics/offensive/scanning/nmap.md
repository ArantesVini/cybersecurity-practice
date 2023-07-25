## NMAP

Unlike all the other tools that sometimes we use or sometime not **nmap** is basically a must use tool for every pentest. Nmap is a _network mapper_, it is used to discorver hosts and services in a network by sending packets and analyze responses.
Since I am running a metasploitable VM on my own network I just run `sudo netdiscover` in order to "figure" the IP of my target, then run nmap to scanning: `nmap [ip and subnet of my vm]`
Is my network, so it run real fast and show me a lot of tcp ports open. True nmap scans will take **hours** to finish!
We got some default ports like SSH, FTP, telnet, but in metasploitable we also got different services, like mysql, postgres and etc. Remember that by default nmap will scan the most commom **1000** ports, not all the 65,000.
To scan all the subnet we can specify by going to 1 to **/24** that represents that **the first three octets doesn't change**.

### Different nmap scan types

#### TCP SYN Scan -sS

To run in terminal use `sudo nmap -sS [url/ip of your target]`. tcp sync scan is the most popular scan type in nmap, it can be performed quickly, scanning **thousands** of ports per second, or networks not protected by a firewall.
It calls TCP SYN scan that onyl peform the **first step of the three-way handhsake**, if the target response with SYN-ACK than that port is listening and open.

### TCP Connection Scan -sT

For -sT **whe don't need root priveleges** so you can use just `nmap -sT [target]`, and estabilishes the full TCP connection with the three way handshake. This scan will leave **much more trace** when you perform it. If you got root priveleges, got with **TCP SYN**

### UDP Scan -sU

UDP scans will be slower, but as the most of the internet is made with TCP sometimes, the people who built the site just ignore UDP. This also requires root priveleges, so `sudo nmap -sU [target]`. If you press the **up arrow key** you can see the % of the scanning, but its really take time, in my example with metasploitable take more than 10 minutos.

## To full understand nmap

Better thatn `nmap --help` is the `man nmap` this is the full manual for nmap, it is a must read thing.
In the curse I am doing it only cover this three scans types, but there is a lot more, that you can check in the manual.

## Discover target OS

To this, your target must have at least **1 open port and 1 closed port**.
The command is `sudo nmap -O [target]`

## Discovering version of a software running on a Open port

To perform version discovery I will use `sudo nmap -sV`, keep in mind that this scan **takes longer** to run than other scans, its a deep scan.
What is the power of this scan? We can simply copy a software version, example in my metasploitble VM who runs a apache web server, just copy the version and google for **vulnerabilities**. Always keep this information in your report!
We can even change the scanning intsinty with `sudo nmap -sV --version-intensity [0-9] [target]` the default value is 7.

## The A is for **Aggressive**

You can pass _-A_ in the bash in order to enable some advanced feature of nmap. This enable OS and version discovering by default, without the need of-O and -sV. And also enable **nmap script scanning**.

## NMAP Scripts
