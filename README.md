UNDER DEVELOPMENT

jadm vet. 0.6

TO BE UPDATED

FreeBSD jail framework with /etc/jail.conf, vnet and zfs support 

At the moment is in development process, still alot of functions should be tested and added.

The idea is to provide jail framewaork wich use only FreeBDS native /etc/jail.conf file
jamd just pars /etc/jail.conf file also use FreeBSD integradted zfs functunality, bsdinstall 
for jail creations (also src) and freebsd jail tools

jadm create custom jail.conf file with initsetup() function (make backup) in order which can be 
parsed also leave availability for /etc/jail.conf custom config.

jadm use zpool and zfs for jail envoirment also bridge interface for vnet network

Requirments:

- 'option vimage' in FreeBSD custom kernel
- already exinsting zpool
- already existing bridge interface with ip address
 (you can use multiple ip's which are used for jails gateways for different network)

Quick install start for beta test:

!! Do not test it in production system !!
If you already use /etc/jail.conf make a copy and delete it , if not exist jadm will create it (!stop all exsiting jails!)

If are not installed:
- pkg install python
- pkg install py27-pip-1.4.1
- pip install tabulate
- pip install netifaces
- pip install ipaddress

Create FreeBSD bridge interface and assign ip address:
- ifconfig bridge1 create
- ifcofnig bridge1 192.168.1.1/24

For second jail network gateway
- ifcofnig bridge1 alias 10.10.10.1/24
- etc ..

To be aveilable on boot in rc.conf add at lease one bridge interface
- cloned_interfaces="bridge1"

bridge ip address ipv4 is used for easy multi ip used for jadm gateways
- ipv4_addrs_bridge1="192.168.1.1/24 10.10.10.1/24"

Add this in /etc/rc.conf if you want to start jails on boot
- jail_enable="YES"                                                                                                                                                                                                                                                              
- jail_parallel_start="YES"                                                                                                                                                                                                                                                      
- jail_list="firstjaisl secondjail "

When jadm is started for first time check if /etc/jail.conf exist and execute initsetup()
When jamd is started check for existing zpool/zfs and bridged interface if they are not available exit with error message

Templates

In ver 0.5 jail was added template usage during jail creation process
Any existing jail can be used like template during jail install process.
Zfs envoirment from exsiting jail is copied in new jail, during this process jadm will create tempoary file 
with original zfs jail content. This file will be created under default jadm zfs folder and after installtion complete  
will be removed (make sure you have enough space)

Changes

ver: 0.6
- a lot of issues with modify function was fixed

var: 0.5 
- existing jail can be used as template during jail creation
-- still in process of development

Any 'bug' which is reported to jadm@dachev.info will help me to speed up development process

