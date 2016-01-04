#!/usr/bin/python
from fabric.api import *
from fabric.context_managers import *
 
env.hosts=['192.168.192.134','192.168.192.137']
env.password='abcd.1234'
env.exclude_hosts=['192.168.192.137'] 
def task1():
    with cd('/root/xxx'):
        run('ls -l')
