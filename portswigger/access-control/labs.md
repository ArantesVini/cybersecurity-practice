# Acces control Labs

## About my system

To solve the labs of access control i use a Kali Linux runnig in a VM.

## Lab 1. Unprotected Admin Funcionality

This is the easiest lab on PortSwigger, just acess the file robots.txt usign the page URI, the file show me the page `administrator-panel`, so I acess this page and remove the user indicated by the Lab (Carlos).

## Lab 2. Unprotected admin funcionality with unpredictable URL

This one don't get neither a /administrator-panel or a robots.txt file, but got a JS script in the HTML code, with a var if the user is Admin create a tag to lead do the admin page, and show the URI of this admin page, each case got a different value, my is `/admin-98aj0efX` (or something like this)
