#!/usr/bin/env python
# JADM python build/install setup file

from setuptools import setup, find_packages
setup(
    name = "jadm",
    version = "0.7",
    packages = find_packages(),
    scripts = ['jadm'],

    # install or upgraded on the target machine
    # - tabulate - used to print useful infomration in table format
    # - netifaces - used for check FreeBSD bridge interfaces
    # - ipaddress - used to check if jail ip is from gateway network

    install_requires = ['tabulate>=0.7', 'netifaces>=0.6', 'ipaddress>=1.0.6', 'paramiko>=1.13.0'],

    # metadata for upload to PyPI
    author = "Nikolay Georgiev Dachev",
    author_email = "jadm@dachev.info",
    description = "JADM is a easy FreeBSD 10 jail framework with /etc/jail.conf, vnet and zfs support ",
    license = "BSD 3-Clause",
    keywords = "jadm vnet zfs jail.conf",
    url = "https://github.com/NikolayDachev/jadm",   # project home page
)
