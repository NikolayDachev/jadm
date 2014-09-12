#!/usr/bin/env python2.7
# JADM python build/install setup file

import os
import sys
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "jadm",
    version = "1.0",
    package_dir = {'': 'lib'},
    packages = ['ipaddress', 'netifaces', 'paramiko', 'tabulate'],
    scripts = ['jadm'],

    # install or upgraded on the target machine
    # - tabulate - used to print useful infomration in table format
    # - netifaces - used for check FreeBSD bridge interfaces
    # - ipaddress - used to check if jail ip is from gateway network
    # install_requires = ['tabulate>=0.7', 'netifaces>=0.6', 'ipaddress>=1.0.6', 'paramiko>=1.13.0'],

    # metadata for upload to PyPI
    author = "Nikolay Georgiev Dachev",
    author_email = "jadm@dachev.info",
    description = ("FreeBSD jail framework"),
    license = "BSD 3-Clause",
    keywords = "jadm vnet zfs jail.conf",
    url = "https://github.com/NikolayDachev/jadm",   # project home page
    long_description=read('README'),
    platforms = ("FreeBSD"),
)

# man page install
if sys.argv[1] == "install":
   os.system('cp ./man8/jadm.8 /usr/local/man/man8/jadm.8')
