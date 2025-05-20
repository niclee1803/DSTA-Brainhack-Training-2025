# Web Service Fundamentals
Web server: computer software that serves web services and pages through HTTP protocol
HTTP protocol: allows exchange of data over internet, requests and responses
Web browser: client software used to access web
Web resource: all contents that exist on web
Cookies: data stored in web browser

# SSL (Secure socket layer)
data is transferred in plain text in HTTP
SSL encrypts data
SSL version of:
HTTP: HTTPS
FTP: SFTP
TELNET: SSH

lock icon to view SSL information (certificate)


# HTTP Request Header
authority, method, path, scheme, accept, cache control and cookie

# HTTP Response Header
content-type is most important (text/html, charset=UTF-8)

# HTTP Request Methods
GET, POST, HEAD, PUT, DELETE
GET: parameter located in the URI
POST: parameter located in HTTP body


# User Agent
in HTTP request header
show which web browser client use

# HTTP Response Status Code
2xx: Success
3xx: Redirection
4xx: Client Error
5xx: Server Error

# nginx
popular open-source web server and reverse proxy
handles client request and forward it to web server
after receiving a response, forward it to client again


more from google:
* Web Server:
NGINX can serve static content (like HTML, CSS, JavaScript, images) and handle HTTP requests, similar to Apache. 
* Reverse Proxy:
NGINX can act as a gateway for web applications, hiding the backend servers from direct internet access. This improves security and performance by caching content, compressing data, and handling SSL/TLS encryption. 
* Load Balancer:
NGINX can distribute incoming traffic across multiple backend servers, preventing any single server from becoming overloaded. 
* Mail Proxy:
NGINX can handle email protocols like IMAP, POP3, and SMTP. 
* Caching:
NGINX can cache static content, reducing load on backend servers and speeding up website loading times. 
* Open Source:
NGINX is free and open-source software, allowing users to customize and extend its functionality. 
* High Performance:
NGINX is known for its event-driven architecture, allowing it to handle many concurrent connections with low resource consumption. 
Why is NGINX popular?
* Scalability:
NGINX is designed to handle high traffic loads efficiently, making it suitable for large-scale websites and applications. 
* Performance:
Its event-driven architecture and low resource consumption contribute to fast response times. 
* Flexibility:
NGINX can be used in various ways, including as a web server, reverse proxy, and load balancer, making it versatile for different needs. 
* Security:
NGINX can help protect backend servers from direct exposure to the internet, improving security. 

