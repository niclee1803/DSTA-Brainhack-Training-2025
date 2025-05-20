# Port Scan
request response for all 65535 possible ports and wait for response
## purpose
attackers: find any port opened unintentionally, reduce attack vector by only attacking open ports
defenders: determine unintended surfaces and take action in advance

## Netstat

```
netstat -nltp
```
uses raw ip packets
-n: output no of ports serviced
-l: filter only listening state
-t: filter only tcp protocol
-p: print program name associated to port

view local open ports only

## Nmap
scan remote host for open ports

### TCP open scan
open port: SYN, SYN+ACK, ACK
closed port: SYN, RST+ACK
form TCP connection (3 way handshake) to verify port is open
leaves log of sesssion establishment in target
```
nmap -sT <ip addr>
```

### SYN scan
open port: SYN, SYN+ACK, RST
closed port: SYN, RST+ACK
stealth scan, does not leave behind any logs
much faster than TCP open scan because no connection process
```
nmap -sS <ip addr>
```

### FIN/NULL/XMAS scan
grouped together as behave very similarly for closed and open ports
open port: FIN, no response
closed port: FIN, RST
FIN: send packets with FIN flag set
NULL: send packets without setting any flags
XMAS: sne dpackets with ACK, FIN, RST, SYN, URG flags set
```
nmap -sF/sN/sX <ip addr>
```

Windows does not follow RFC 793 for these scan types — it responds with RST regardless of port status.


CDDC2025{p4ck3t_1nspect10n_********_*********_*********}