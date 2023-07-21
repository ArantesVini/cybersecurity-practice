# SQL Injection - A Cybersecurity Study

## Introduction

SQL injection is a common and critical vulnerability found in web applications that interact with a database. It occurs when untrusted user input is improperly handled and allows an attacker to execute malicious SQL queries, potentially gaining unauthorized access to the database or compromising sensitive data. This GitHub repository serves as a documentation of various SQL injection techniques tested on PortSwigger Web Security Academy.

## SQL Injection Allowing Login Bypass

**Objective: Bypass the login for the 'administrator' account when the password is unknown.**

1. Access the login page of the lab.
2. Attempt to log in with the username 'administrator' and input a single quote (') in the password field.
   - Example: Username: `administrator`, Password: `'`
3. If the login attempt results in an internal server error, it indicates a possible SQL injection vulnerability.
4. Now, utilize a SQL comment command `--` after the single quote in the password field to bypass the password check.
   - Example: Username: `administrator`, Password: `'--`
5. With the SQL comment, any password we enter after `--` will allow us to log in as the administrator.
   - Example: Username: `administrator`, Password: `'--any_password`

## SQL Injection UNION Attack. Retrieve Data From Other Tables

**Objective: Retrieve all users and password information, to login administrator account**

1. Change the category filter, altering the URL;
2. Inject a single-quote after the filter to perform a SQL command;
3. Use `UNION SELECT * FROM users;` to retrieve the user data, including the administrator password.

## SQLmap - A Powerful SQL Injection Tool

SQLmap is a potent tool for discovering weaknesses in web applications and retrieving data from databases:

1. Use `sqlmap -u [url] --dbs` to list the available databases.
2. Fetch the tables using `sqlmap -u [url] -D [db_name] --tables`.
3. View the columns in a specific table with `sqlmap -u [url] -D [db_name] -T [table_name] --columns`.
4. Retrieve data from the columns specified with `sqlmap -u [url] -D [db_name] -T [table_name] --columns "[columns_names]" --dump`. \*Place all column names in the same double quotes\*: "column_1,column_2".

SQLmap can also be used to identify potential vulnerabilities in a web application for SQL injection exploitation.

## SQL Injection Types

### Error-Based Injection

Force the database to generate error messages, revealing information about the data.

**In SQLMAP**, use the parameter `E`.

### Time-Based Injection (Blind Query)

Perform a blind query without directly seeing the database information, relying on response time. For example, `id=A' waitfor delay '00:00:10'--`

**In SQLMAP**, use the parameter `T`.

### Stacked Queries

Perform an injection to modify the data and execute a new query simultaneously.

**In SQLMAP**, use the parameter `S`.

### Boolean-Based Injection (Blind Query)

Another type of blind query injection where boolean conditions are used to fetch data from the database.

**In SQLMAP**, use the parameter `B`.

### Union Query-Based Injection

Perform a **UNION SELECT** to fetch data from another table.

**In SQLMAP**, use the parameter `U`.

### Command Injection

Exploit application vulnerabilities to access the shell and execute command lines.

**In SQLMAP**, use the parameter `Q`.

## Note

**Note**: In a real-world scenario, exploiting SQL injection vulnerabilities is illegal and unethical. Only perform such actions in environments where you have explicit permission to do so.

Remember to responsibly disclose any security vulnerabilities you may discover.
