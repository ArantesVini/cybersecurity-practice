# Basic conecpts in Deffensive Security

## DNS - Domain Name System

The Domain Name System (DNS) plays a crucial role in the functioning of the internet. Its primary purpose is to translate human-readable domain names (like www.example.com) into IP addresses, which are numerical values used to identify and locate devices on the internet. DNS doesn't host websites or applications; instead, it ensures that requests are directed to the correct destination.

## Remote access protocols

### Telnet

Telnet is a remote access protocol that allows users to interact with a device or server over a network. However, it lacks built-in encryption, meaning that all data sent through Telnet is transmitted in plain text. This creates a significant security risk, as any malicious entity intercepting the communication can easily read and compromise the data. The vulnerabilities in Telnet make it susceptible to attacks like **"Man-in-the-Middle"**, where an attacker secretly relays and possibly alters the communication between two parties, and **"sniffers"**, which capture and analyze network traffic.

### SSH (Secure Socket Shell)

SSH is a secure remote access protocol widely used in cybersecurity. It provides encrypted communication between the client and server, ensuring that data transmitted between them remains confidential and protected from eavesdropping. The encryption used in SSH ensures that only the intended recipient, the server, possesses the means to decrypt and understand the data. This makes SSH a much more secure alternative to Telnet, as it mitigates the risks associated with transmitting sensitive information over a network in plain text.

By adopting SSH and avoiding Telnet usage, individuals and organizations can significantly enhance their defensive security posture, protecting their data and systems from potential threats and unauthorized access.
