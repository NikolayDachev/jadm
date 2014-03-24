JADM is a easy FreeBSD 10 jail framework with /etc/jail.conf, vnet and zfs support 

At the moment is in development process, still alot of functions should be tested and added.
!! Use it in production system on your own risk !!
Any 'bug' which is reported to jadm@dachev.info will help me to speed up development process

Information:

Jadm provide jail framework wich use only FreeBDS native /etc/jail.conf file
jamd just pars /etc/jail.conf file also use FreeBSD integradted zfs functionality, bsdinstall 
for jail creations (also src) and freebsd jail tools.
Jadm create custom /etc/jail.conf file with initsetup() function (make a backup if /etc/jail.conf exist)
jadm use zfs for jail envoirment also bridge+epair interfaces for vnet(vimage) network

Requirments:

- 'option vimage' in FreeBSD custom kernel
- already exinsting zpool
- already existing bridge interface with ip address (you can use multiple ip's which are used for jails gateways for different network)

Quick install:

If are not installed:
- pkg install python
- pkg install py27-pip

"Install via setup.py"
- python setup.py build
- python setup.py install

"Install via FreeBSD port .. should be tested"
- cd ./FreeBSD
- make install

Create FreeBSD bridge interface and assign ip address:
- ifconfig bridge1 create
- ifcofnig bridge1 192.168.1.1/24

For second jail network gateway
- ifcofnig bridge1 alias 10.10.10.1/24
- etc ..

To be aveilable on boot in rc.conf add at lease one bridge interface:
- cloned_interfaces="bridge1"
bridge ip address ipv4 is used for easy multi ips - jadm gateways
- ipv4_addrs_bridge1="192.168.1.1/24 10.10.10.1/24"

Add this in /etc/rc.conf if you want to start jails on boot
- jail_enable="YES"                                                                                                                                                                                                                                                              
- jail_parallel_start="YES"                                                                                                                                                                                                                                                      
- jail_list="firstjaisl secondjail "

When jadm is started for first time check if /etc/jail.conf exist and execute initsetup()
When jamd is started check for existing zpool/zfs and bridged interface if they are not available exit with error message

For more details how to use jadm please check help funciton or jadm man (8) page
