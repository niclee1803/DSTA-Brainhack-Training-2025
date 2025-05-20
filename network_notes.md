# What happens when you type example.com in your browser
DNS Query to find IP address of server wehre example.com is being serviced
If there is already cached data, corresponding IP address will be returned immediately
2-7: recursive query processes performed by the DNS resolver
Root server -> TLD (.com DNS server) -> DNS server that manages example.com)
IP address delivered to user
User can send HTTP request to server using IP address.