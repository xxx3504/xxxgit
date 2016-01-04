from fabric.api import run, env
env.hosts = ['192.168.192.134', '192.168.192.137']
def taskA():
    run('ls')
def taskB():
    run('whoami')
