
    PLEASE TRY JADM 2.0, STILL IN DEVELOPMENT BUT WITH MUCH BETTER FUNCTIONALITY, ALSO JADM 1.0 WILL BE ABANDONED VERY SOON
    FOR NOW YOU CAN CHECK HELP HOW TO USE IT
    https://github.com/NikolayDachev/jadm2_test/ 

Jadm is python script which pars /etc/jail.conf in his own format. Jadm use  zfs  for  jail home also bridge interface and epair interfaces for jail vnet.

For more details please check jadm(8) man pages and 'help' command 

Quick start:

Custom FreeBSD kernel for vnet support:

    options         VIMAGE

If are not installed:

    pkg install python27
    pkg install py27-pip

Install via setup.py:

    ./setup.py build
    ./setup.py install

Create FreeBSD bridge interface and assign ip address:

    ifconfig bridge1 create
    ifconfig bridge1 192.168.1.1/24
    ifconfig bridge1 alias 10.10.10.1/24
    etc ..

IPFW Nat setup:

    ipfw add divert 8668 ip from any to any via (external interface)

Example FreeBSD config:

/etc/rc.conf

    cloned_interfaces="bridge1"
    ipv4_addrs_bridge1="192.168.1.1/24 10.10.10.1/24"

    gateway_enable="YES"
    arpproxy_all="NO"

    firewall_enable="YES"
    firewall_script="/etc/ipfw.conf"
    natd_enable="YES"
    natd_flags="-f /etc/natd.conf"

    jail_enable="YES"
    jail_parallel_start="YES"
    jail_list="firstjaisl secondjail "

/etc/natd.conf

    interface (external interface)
    dynamic yes
    same_ports yes

/etc/ipfw.conf
 
    #!/bin/sh

    fwcmd="/sbin/ipfw -q"
    eif="(external interface)"

    ${fwcmd} -f flush

    ${fwcmd} add 65532 divert natd ip from any to any via ${eif}
    ${fwcmd} add 65533 allow ip from any to any
