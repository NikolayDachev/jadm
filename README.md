jadm
====

UNDER DEVELOPMENT

FreeBSD jail framework with /etc/jail.conf, vnet and zfs support

SHORT INSTALL PROCESS:

jadm required packages: 

pkg install python
pkg install py27-pip-1.4.1

pip install tabulate
pip install netifaces

 in rc.conf add at lease one bridge interface
cloned_interfaces="bridge1"

 asain bridge ip address ipv4 is used for easy multi ip used for jadm gateways
ipv4_addrs_bridge1="192.168.1.1/24"

 create at lease one zfs zpool (you can use and existin one)
During the initsetup jadm will check for existing bridge interface and existing zpools
also it will check for existing /etc/jail.conf and will make a backup (jadm is in development proces please make a backup before start initsetup)

You need and "option vimage" in you kernel .. rebuild it if is needed in order to have vnet support

If you start jadm for first time jadm will execute initsetup automaticaly

................. jadm is in development process do not use it in production system ..............................................................
................. please test it on your own risk also i will appreciated any bug reported to <jadm@dachev.info>...................................

Please check jadm "help" command, this application was created with idea to be maximum easy for usage.

This README will be updated asap when i have a time.                 

