# XSS Labs and Studies

## Cross-Site Scripting (XSS) - A Critical OWASP Top Ten Web Application Security Risk

Cross-Site Scripting (XSS) is a prevalent and dangerous OWASP Top Ten Web Application Security Risk that plagues web applications worldwide.

XSS occurs when attackers inject malicious scripts into web pages that are viewed by other users. These scripts execute within the victims' browsers, allowing the attacker to steal sensitive information, hijack user sessions, deface websites, deliver malware, and carry out various other malicious actions. As a client-side vulnerability, XSS poses a significant risk to both users and the web application itself.

## Lab 1. Reflected XSS into HTML context without nothing encoded

**Objective:** Call a `alert` function

1. The page got a search field;
2. In this search field we can pass a HTML tag `<script></script>`;
3. As your objetive is really simples, just use the alert function: `<script>alert('Have you heard about the high elfs?')</script>`.

**\*Important** someone with bad intetions can send this URLs with XSS scripts (hidden) as a form of social engineering!

## Lab 2. Stored XSS into HTML context without nothing encoded

**Objective:** Call the `alert` function when a post is viewed

1. Select a post;
2. We got a comment section, so is the perfect palce to store the script;
3. Use the tag `<script>alert('Have you heard about the high elfs?')</script>` as comment with a random email and name.

**Remember** this is a example of **XSS Persist**, we can share the page with the post where I perform the XSS and another user on another machine also will get the alert.

## Lab 3. DOM XSS in `document.write` sink using source `location.search`

**Objective:** Call the alert function

1. After you try to search something and inspect the DOM you see a `<img>` tag that search for the input;
2. You can break this tag by closing it before in the search field and comment the end;
3. Between the closing and the comment you can add a `<script>` tag to call the alert function;
4. Simply by inputing `>  <script>alert(1)</script>//`

**Note** DOM XSS only execute the script on user machine, not in the server, who does not receive anything.
**Warning** When a site applies encoding a person with bad intentions can use ` &lt; script &gt;` where `&lt` stands for `<` and `&gt` for `>`.
