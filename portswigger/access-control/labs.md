# Access Control Labs and Studies

## Access Control - An OWASP Top Ten Web Application Security Risk

Access Control is a fundamental cybersecurity concept that plays a crucial role in safeguarding digital assets and protecting sensitive information from unauthorized access and misuse. This GitHub repository aims to provide an in-depth exploration of access control mechanisms, their importance, and best practices to implement robust access control strategies for various systems and applications.

Improper access control can lead to unauthorized access to sensitive functionality, data, or resources within a web application. Attackers can exploit these vulnerabilities to escalate privileges, gain unauthorized access to other users' accounts, or manipulate data and functionalities beyond their intended scope. As a result, access control misconfigurations pose a significant threat to the confidentiality, integrity, and availability of web applications.

## About My System

To solve the access control labs, I use Kali Linux running in a virtual machine (VM).

## Lab 1. Unprotected Admin Functionality

**Objective: Delete the user Carlos**

This is the easiest lab on PortSwigger. First, access the file `robots.txt` using the page URI. The file will reveal the page `administrator-panel`. Proceed to this page and remove the user indicated by the lab (Carlos).

## Lab 2. Unprotected Admin Functionality with Unpredictable URL

**Objective: Delete the user Carlos**

In this lab, there is no `/administrator-panel` or `robots.txt` file, but the HTML code contains a JavaScript variable that determines the admin page URL. The value varies for each user. My URL was `/admin-98aj0efX` (or something similar).

## Lab 3. User Role Controlled by Request Parameter

**Objective: Delete the user Carlos**

To solve this lab, I utilized the community edition of Burp Suite with the Proxy Interceptor. Follow these steps:

1. Access the login screen and use the user `wiener:peter`.
2. On the change email screen, use Burp Suite to intercept the request and inspect the cookies sent to the proxy.
3. One of the cookies will have the value `admin=false`. Modify it to `admin=true`, forward the request, and update the user's role to admin.
4. By changing the `admin` cookie to `true`, you can access the Admin panel and easily delete Carlos again.

## Lab 4. User Role Can Be Modified in User Profile

**Objective: Delete the user Carlos**

For this lab, I once again used Burp Suite. Follow these steps:

1. Go to the change email screen, and intercept the request using Burp Suite.
2. Send the intercepted request to the Repeater, where you can modify the JSON payload to change your `roleid` to `2`.
3. Forward the modified request through the Proxy, disable the interceptor, and reload the page.
4. After these steps, you will be able to easily delete Carlos.

# New Tools

**Wapiti**: Wapiti can be used to perform a sweep on the URL. Use the command `wapiti -u [url]`.

**Wappanalyzer**: Wappanalyzer is a browser extension that helps recognize webpage technologies.

**Cookie Manager**: This extension allows you to retrieve cookies from webpages. For example, in Lab 3, you can obtain the profile URL and change the `Admin` cookie to `true`.
