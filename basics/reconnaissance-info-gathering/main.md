# What is Information Gathering?

Simples as the name, gathering information about your target, we can divide it into two types.

## Types of information gathering

- Active: Using your machine we try to get as much data or as much information whilete **interacting with them**

- Passive: We will use a intermediate system, AKA **Middle Source** to get the information about your target, like googling about your target, talk to someone, acessing another website etc.

## The Goals of Information Gathering

First of all identify the target and ip Adress / Adresses, employees emails /phone numbers, but the main goal is to fin **technologies** the target has, in a company we want to know how many networks they have, what softwares are running, OS they have.

## Tools for information gathering

**ping, nslookup, whois, whatweb**

For this we can do activly or passivly.

For active information gathering

1. use `ping [url]`
   Importante that the url **must be without any http/https or www.**

Even if we don't get any response we will get the **IP Adress**, most of the websites will blocking ping probes.

2. `nslookup [url]`
   This will just output the ip adress of the website you passed.

For passive info gathering you can just look for a website that show another websites IP adress, like **ipinfo.info**, ipinfo even show informations like phisical adress, expiration of the domain and etc.

Another powerful tool to do this is **whois**, already installed on kali linux.

3. WHOIS

Whois is run by the terminal by `whois [url]` and the output will got information like the person name and email, DNS server, domain information, phisical adress, and sometimes even the owner document.

4. Whatweb

First of all is important to tell that **whatweb** got a "stealthy" version that we can use in any site, thatj ust send one HTTP request, but got more aggressive modes that we can just use in pentest. To use simply type `whatweb [url]` this will use the default level of `--aggression`, 1 is the stealthy one, that send one http request.

This version will already output to us the server, where it is, languages uses, cookies etc. With verbose mode `--verbose` or `-v` we will get a better version to read, also with plugin descriptions.

We can also use whatweb to scan a network range, by `whatweb xxx.xxx.x.1-xxx.xxx.x.255` in example of a netmask to go from 1 to 255, the usual.

By this we can perform a `--aggression=3` in my own net, if i got some page run on my network this will output even **password field**, in a pentest this could be used in a brute force attack.
In a big range of network we can use `--no-errors` at the end to prevent the _No route to host_ error, of offline ip adress.

## Gathering email from a company or domain
