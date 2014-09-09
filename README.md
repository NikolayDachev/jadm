Jadm is python script which pars /etc/jail.conf in his own format. Jadm use  zfs  for  jail home also bridge interface and epair interfaces for jail vnet.

For more details please check jadm(8) man pages and 'help' command 

Quick start:

Custom FreeBSD kernel for vnet support:

    options         VIMAGE

If are not installed:

    pkg install python
    pkg install py27-pip

Install via setup.py:

    python setup.py build
    python setup.py install

Install via FreeBSD port .. should be tested:

    cd ./FreeBSD
    make install

Create FreeBSD bridge interface and assign ip address:

    ifconfig bridge1 create
    ifcofnig bridge1 192.168.1.1/24
    ifcofnig bridge1 alias 10.10.10.1/24
    etc ..

To be aveilable on boot in rc.conf add at lease one bridge interface:

    cloned_interfaces="bridge1" 
    ipv4_addrs_bridge1="192.168.1.1/24 10.10.10.1/24"

Add this in /etc/rc.conf if you want to start jails on boot

    jail_enable="YES"
    jail_parallel_start="YES"
    jail_list="firstjaisl secondjail "
