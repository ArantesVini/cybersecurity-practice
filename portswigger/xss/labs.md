# XSS Labs and Studies

## Cross-Site Scripting (XSS) - A Critical OWASP Top Ten Web Application Security Risk

Cross-Site Scripting (XSS) is a prevalent and dangerous OWASP Top Ten Web Application Security Risk that plagues web applications worldwide.

XSS occurs when attackers inject malicious scripts into web pages that are viewed by other users. These scripts execute within the victims' browsers, allowing the attacker to steal sensitive information, hijack user sessions, deface websites, deliver malware, and carry out various other malicious actions. As a client-side vulnerability, XSS poses a significant risk to both users and the web application itself.

## Lab 1. Reflected XSS into HTML context without nothing encoded

**Objective:** Call a alert function

1. The page got a search field;
2. In this search field we can pass a HTML tag `<script></script>`;
3. As your objetive is really simples, just use the alert function: `<script>alert('Have you heard about the high elfs?')</script>`.
   ß
