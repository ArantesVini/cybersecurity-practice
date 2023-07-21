# SQL Injection

## SQL Injection Allowing Login Bypass

**Objective: Bypass the login for the 'administrator' account when the password is unknown.**

1. Access the login page of the lab.
2. Try to log in with the username 'administrator' and input a single quote (') in the password field.
   - Example: Username: `administrator`, Password: `'`
3. If the login attempt results in an internal server error, it indicates a possible SQL injection vulnerability.
4. Now, use a SQL comment command `--` after the single quote in the password field to bypass the password check.
   - Example: Username: `administrator`, Password: `'--`
5. With the SQL comment, any password we enter after `--` will allow us to log in as the administrator.
   - Example: Username: `administrator`, Password: `'--any_password`

**Note**: In a real-world scenario, exploiting SQL injection vulnerabilities is illegal and unethical. Only perform such actions in environments where you have explicit permission to do so.

Remember to responsibly disclose any security vulnerabilities you may discover.
