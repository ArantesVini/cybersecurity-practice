# What is Information Gathering?

Simples as the name, gathering information about your target, we can divide it into two types.

## Types of information gathering

- Active: Using your machine we try to get as much data or as much information whilete **interacting with them**

- Passive: We will use a intermediate system, AKA **Middle Source** to get the information about your target, like googling about your target, talk to someone, acessing another website etc.

## The Goals of Information Gathering

First of all identify the target and ip Adress / Adresses, employees emails /phone numbers, but the main goal is to fin **technologies** the target has, in a company we want to know how many networks they have, what softwares are running, OS they have.

## Tools for information gathering

### How identify your target and get its IP adress

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
