# Client-side security issues
XSS
CSRF
Client-side authentication
Open redirect

# Server-side security issues
SQL Injection
SSRF
Local file inclusion
Path traversal


OWASP Top 10: list of 10 web security vulnerabilities that can have an impact on security, being updated every 3-4 years regularly


# Injection
includes SQL, OS command, LDAP injection
occurs when web app uses user input without validating it

# Server-side Request Forgery (SSRF)
make a server send requests to another server
occurs when web app fetches a remote resource without validating URL provided by user
can access remote server

Authentication: verifying identity of user, usually done by passwords
Authorisation: verifying applications and data user can access, takes place after authentication always


# Client side Authentication
can be easily manipulated
Javascript is a client side language
Never authenticate using Javascript, authenticate on server side instead

# Local file inclusion (LFI)
include files that are locally present on the server
can occur when a page receives the path to the file that has to be included as a user input

# Path Traversal
allows attackers to access files on web server they should not access
can call other APIs by accessing parent path andc traverse server
Bypass techniques:
* ../../../../
* ..%2f (URL-encoded version of /), some sites will filter common path traversal payloads such as ../
* %2e%2e%2f (../)
* ..\ (windows uses backslash to separate directories unlike linux)
* ..%5c
* %2e%2e%5e
* %252e%252e%2255c (URL-encoded version of above), bypass website filters, some websites decode once to filter

# File upload vulnerability
upload file to server through web service
If server has file upload vulnerability, attacker can upload malicious file to server's file system
If users can upload arbitrary file to web service operating directory, they can execute arbitrary code on the server

OS commands may be executed with functions supported by the web application language (Webshell)
