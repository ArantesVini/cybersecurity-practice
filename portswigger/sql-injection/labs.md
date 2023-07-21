# SQL Injection

## SQL Injection Allowing login bypass

Objective: bypass the login, the username is administrator but we don't know the password.

After enter the lab in the login page, when we try to login the administrator profile we can simple put a single qote to lead a internal server error, if after this qote we put a SQL comment command `--` and any password we get in.
