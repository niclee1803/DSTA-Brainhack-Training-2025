# Open source intelligence
CPA: Collection, processing, analysis
Secure mail and browser
Proxy and privacy

## Secure mail: Protonmail
data encrypted
anonymous or temporary email works as well

## Secure browser
Chrome, Edge, Safari: passwords, cookies, credit card info saved

## VPN
can be hacked, used Torsocks

## Torsocks
Install
```
sudo apt-get install tor
```

```
torsocks
```

Get your IP address
```
wget -qO- http://ipecho.net/plain ; echo
```
wget is a command line that web requests and responds to

change ip
```
torsocks wget -qO- http://ipecho.net/plain ; echo
```

Check ip again
```
wget -qO- http://ipecho.net/plain ; echo
```

End
```
sudo killall -9 tor
```


## Anonymous avatar
can use anonymous SMS



# Shodan: search engine for internet connected devices
gathers info about all devices directly connected to the internet
filters: city, country, geo, hostname, net, os, port
before and after filters can only be accessed through command line


# Censys: search engine for finding internet devices such as computers, servers, and smart devices
login is required to access full capabilities of the tools
limited searches can be performed without authentication

has pre-built search queries, including by port no, protocol no, and request and return value (80.http.get.status_code:404)

## Dark Web and Deep Web
Tor, I2P, Freenet, ZeroNet
Deep web: need authentication
Dark web: need special software
Onion, layers of anonimity


## Google Hacking
sometimes vulnerabilities may appear on search engine indexes
Exploit database: google hacking database


## Maltego: OSINT tool that helps users collect data more easily by showing data collection part in form of visualised graph
CE License: free
3 type of server for collecting data: CTAS, iTDS, Comms
CTAS: includes all transforms found on Paterva's public server
iTDS: allows managing company's information and internal information
Comms: same graph with multiple users at once


Entity: node (phone no, dns name, person etc)
Transform: piece of code that takes one entity to another, relationship. done by querying a data source and returning results as new entities on graph. sources include: DNS servers, search engines, social networks, WHOIS
Machine: chain of multiple transforms that are automated and run together (similar to Macro)

Transform hub: install and manage third-party transforms

### Use cases:
Create connections to find hidden correlations

### Local transforms
user can change entire code of local transform, only runs on user's machine and not Maltego server
create code, establish project, set up environment, run

GoogleHunt:
xeuledoc: python module which fetches info about any public Google document

enter document ID -> get info about the google document

need Python3
install following modules
```bash
pip3 install maltego-trx // for local transform project management
pip3 install xeuledoc
pip3 install requests // allow sending of http requests using python
```

test xeuledoc module
```bash
xeuledoc <Google document link>
```

start to create a local transform in mytransform folder
```
maltego-trx start mytransform
```
transform folder: python scripts
add new local transform, select Phrase in input entity type, set working directory to mytransform
input command line
```bash
python.exe project.py local googlehunt "Entity Value" "field1=field1 value#field2=field2 value"
```

## Machines
aka transform macros
runs multiple transforms on a dataset



CDDC2025{collect_validate_analyze_document_secure_share_standby_repeat}

