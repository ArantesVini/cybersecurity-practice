# Acces control Labs

## About my system

To solve the labs of access control i use a Kali Linux runnig in a VM.

## Lab 1. Unprotected Admin Funcionality

Objective: Delete the user **Carlos**
This is the easiest lab on PortSwigger, just acess the file robots.txt usign the page URI, the file show me the page `administrator-panel`, so I acess this page and remove the user indicated by the Lab (Carlos).

## Lab 2. Unprotected admin funcionality with unpredictable URL

Objective: Delete the user **Carlos**
This one don't get neither a /administrator-panel or a robots.txt file, but got a JS script in the HTML code, with a var if the user is Admin create a tag to lead do the admin page, and show the URI of this admin page, each case got a different value, my is `/admin-98aj0efX` (or something like this)

## Lab 3. User Role Controlled by request parameter

Objective: Delete the user **Carlos**
For this lab I use the community edition of Burp Suite to use the Proxy Interceptor
First I got to the Login screen and use the user wiener:peter, after in the change email screen i use the Burp Suite to check the cookies sended to the proxy, one of the cookies is admin=false, so I changed it to true, send the request, changed it to true in the user screen and now I got access to Admin panel, where I just keep changing the cookie admin=true and then delete Carlos again!

## Lab 4. User Role can me modified in User Profile

Objective: Delete the user **Carlos**
For this lab, again I will use Burp Suite. Got again to change email screen and send the proxy request and send the proxy response to the repeater, where I change the JSON passed to the server to change my roleid=2, send again the requisition on Proxy, disable the interceptor and reload the page, after that I can ease deleter Carlos!
