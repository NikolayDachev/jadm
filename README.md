UNDER DEVELOPMENT

jadm vet. 0.25

TO BE UPDATED

FreeBSD jail framework with /etc/jail.conf, vnet and zfs support 

At the moment is in development process, still alot of functions should be tested and added.

The idea is to provide jail framewaork wich use only FreeBDS native /etc/jail.conf file
jamd just pars /etc/jail.conf file also use FreeBSD integradted zfs functunality, bsdinstall 
for jail creations (also src) and freebsd jail tools

jadm create custom jail.conf file with initinstall function (make backup) in order which can be 
parsed also leave availability for /etc/jail.conf custom config.

jadm use zpool and zfs for jail envoirment also bridge interface for vnet network

Requirments:

- 'option vimage' in FreeBSD custom kernel
- already exinsting zpool
- already existing bridge interface with ip address
 (you can use multiple ip's which are used for jails gateways for different network)

Quick install start for beta test:

If are not installed:
- pkg install python
- pkg install py27-pip-1.4.1
- pip install tabulate
- pip install netifaces

Create FreeBSD bridge interface and assign ip address:
- ifconfig bridge1 create
- ifcofnig bridge1 192.168.1.1/24

To be aveilable on boot in rc.conf add at lease one bridge interface
- cloned_interfaces="bridge1"

bridge ip address ipv4 is used for easy multi ip used for jadm gateways
- ipv4_addrs_bridge1="192.168.1.1/24"

Any 'bug' which is reported to jadm@dachev.info will help me to speed up development process


