# Sniffing
monitoring all data packets passed through network
hub environment: packets forwarded to everyone, just enable promiscuous mode
switch environment: point to point, need additional action. use methods such as attacking ARP protocol to carry out active attack
Promiscuous mode has to be enabled for sniffing in a hub environment
Promiscuous mode: mode that accepts all packets, all interfaces in the network can acccept all traffic received regardless of destination
```
ifconfig eth0 promisc
```

Wireshark: network analysis tool

Wireshark filtering
ip.addr: filter out ip addresses
ip.src/ip.dst: source or destination
eth.src/eth.dst/eth.addr: MAC addresses
tcp.srcport/tcp.dstport/tcp.port: Port


CDDC2025{p4ck3t_1nspect10n_f1rew4ll_1ntrus10n_d3t3ct10n}