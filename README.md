JADM is a easy FreeBSD 10 jail framework with /etc/jail.conf, vnet and zfs support 

At the moment is in development process, still alot of functions should be tested and added.

!! Use it in production system on your own risk !!

Any 'bug' which is reported to jadm@dachev.info will help me to speed up development process

Information:

Jadm provide jail framewaork wich use only FreeBDS native /etc/jail.conf file
jamd just pars /etc/jail.conf file also use FreeBSD integradted zfs functunality, bsdinstall 
for jail creations (also src) and freebsd jail tools.
Jadm create custom jail.conf file with initsetup() function (make a backup if /etc/jail.conf exist)
jadm use zfs for jail envoirment also bridge interface for vnet network

Requirments:

If are not installed:
- pkg install python
- pkg install py27-pip
- pip install tabulate
- pip install netifaces
- pip install ipaddress

- 'option vimage' in FreeBSD custom kernel
- already exinsting zpool
- already existing bridge interface with ip address
 (you can use multiple ip's which are used for jails gateways for different network)

Quick install:

Create FreeBSD bridge interface and assign ip address:
- ifconfig bridge1 create
- ifcofnig bridge1 192.168.1.1/24

For second jail network gateway
- ifcofnig bridge1 alias 10.10.10.1/24
- etc ..

To be aveilable on boot in rc.conf add at lease one bridge interface
- cloned_interfaces="bridge1"
bridge ip address ipv4 is used for easy multi ips - jadm gateways
- ipv4_addrs_bridge1="192.168.1.1/24 10.10.10.1/24"

Add this in /etc/rc.conf if you want to start jails on boot
- jail_enable="YES"                                                                                                                                                                                                                                                              
- jail_parallel_start="YES"                                                                                                                                                                                                                                                      
- jail_list="firstjaisl secondjail "

When jadm is started for first time check if /etc/jail.conf exist and execute initsetup()
When jamd is started check for existing zpool/zfs and bridged interface if they are not available exit with error message

Jadm Help:

- initsetup - Initial JADM setup
You can start initseup manualy

- setup - Modify JADM setup
You can change jadm defaul folder/zfs also default bridge interface
If you change default jadm folder all jails zfs path will be renamed automaticaly to new location 
If you change default bridge interface you should modify all jails manually to use correct network
  
- help - This help information
Show jadm help information  

- about - About JADM
Show jadm version and license information

- exit or '!' - exit from JADM
Exit from jadm

- create - Create new Jail 
Easy interactive way to create new jail:
Jail Name:>  this name will be used also for jail zfs 
Jail Hostname:> jail hostname example: jail.local.lan
Jail ID:> jail ID also will be used also for jail epair inteface number (vnet / bridge interface conection)
Jail Gateway number:>  show brige interfaces asignet ip addresses which are used for jail default gatway and jail network just select a number
Jail IP Address:>  jail ip address, also jadm check if this ip address is from selected default gateway network
Jail ZFS Quota (M)egabytes, (G)igabytes, (none) for unlimited:> enter zfs quota for jail use none if quota is not needed example: 10G

After all required data is entered jadm will show summarise config and will ask for confirmation (y/n)
In this stage jadm will create zfs path for your jail if this zfs path already exist jadm will ask who to proceed
(recreate) - will destroy zfs path and existing data and will create new one with same name 
(use) - will use existing zfs path (jail environment) and will complete installation

install source:> 
(template) - jadm will use existing jail like a template and will ask for jail name (only name work) 

Any existing jail can be used like template during install process.
ZFS environment from existing jail will be copied in new jail, during this process jadm will create temporary file "jadm_temp_file" with original zfs content.
This file will be created under default jadm zfs folder and after installtion complete will be removed (make sure you have enough space)
(The process is not realy fast but avoid zfs snapshot hierarchy)
Also jadm will copy ### jail local options ### section from template jail to new one

(bsd) - jadm use bdsinstaller which is similiar to new freebsd instalation 
During this process bsdinstaller will use internet to donwload FreeBSD pkg's

(src) - jadm will try to build jail environment from sources /usr/src, it will ask to make new buildworld or to use already existing builded sources

After jail install complete jadm will execute post install function with default settings for jail /etc/rc.conf and /etc/resolv.conf

/etc/jail.conf
sendmail_enable="NONE"
firewall_enable="YES"
firewall_script="/etc/rc.firewall"
firewall_type="OPEN"

/etc/resolv.conf
nameserver 8.8.8.8

- destroy - Destroy existing Jail and delete Jail data/zfs (usage: destroy 'jailname or jid')
Will remove jail config from /etc/jail.conf and will destroy jail zfs data (all jail data will be deleted) 
 
- remove - Remove existing Jail but keep Jail data/zfs (usage: remove 'jailname or jid')
Will remove jail config from /etc/jail.conf but will keep jail zfs data which can be used for new jail

- modify -  Modify existing Jail (usage: modify 'jailname or jid')
You can easy modify existing jail settings (name, hostname, jid, gateway, ip addr and zfs quota)

- listsnap -  Jail ZFS snapshots list (usage: listsnap 'jailname or jid')
- createsnap -  Create new Jail ZFS snapshot (usage: createsnap 'jailname or jid')
Create jail zfs snapshot with special data/time number at the end
 
- restoresnap -  Restroe Jail ZFS from snapshot (usage: restoresanp 'jailname or jid')
Select snapshot number from list which should be restored 
!!! If jail zfs will be restored from older snapshot all newer snapshots will be destroyed !!!

- rmsnap -  Remove Jail ZFS snapshot (usage: rmsanp 'jailname or jid')
- start - Start Jail (usage: start 'jailname, jid or all')
-  stop - Stop new Jail (usage: stop 'jailname, jid or all')

- list - List Jails on the system (usage: list 'jailname or jid' / only 'list')
list jail name/jid will show selected jail configuration

- shell - Enter in Jail (usage: shell 'jailname, jid or all')
- gateways - List available Jail gateways on the system
