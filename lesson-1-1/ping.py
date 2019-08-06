import subprocess
import ipaddress
from pprint import pprint
from tabulate import tabulate


def host_ping(hosts, silent=False):
    reachable = []
    unreachable = []
    for host in hosts:
        str_host = str(host)
        p = subprocess.Popen( ['ping', str_host] , shell=True , stdout=subprocess.PIPE)
        out = p.stdout.read()
        msg = out.decode('utf-8')
        if msg.find(r'100% loss') == -1 and msg.find(r'100% потерь') == -1 and msg.find(r'unreachable') == -1 and msg.find(r'недоступен') == -1:
            if not silent:
                print(f'Host {str_host} is reachable')
            reachable.append(str_host)
        else:
            if not silent:
                print(f'Host {str_host} is unreachable')
            unreachable.append(str_host)
    return {'reachable': reachable, 'unreachable': unreachable}
hosts = [
    'mail.ru', 
    ipaddress.ip_address('192.168.0.1'), 
    ipaddress.ip_address('10.0.0.1')
]
host_ping(hosts)
# Host mail.ru is reachable
# Host 192.168.0.1 is reachable
# Host 10.0.0.1 is unreachable

def host_range_ping(ipRange):
    host_ping(ipRange)

def host_range_ping_tab(ipRange):
    dicts_list = host_ping(ipRange, silent = True)
    print(tabulate(dicts_list, headers='keys' , tablefmt="grid" )) 

subnet = ipaddress.ip_network( '192.168.0.0/29' )
ipRange = list(subnet.hosts())

host_range_ping(ipRange)
# Host 192.168.0.1 is reachable
# Host 192.168.0.2 is unreachable
# Host 192.168.0.3 is unreachable
# Host 192.168.0.4 is unreachable
# Host 192.168.0.5 is unreachable
# Host 192.168.0.6 is unreachable

host_range_ping_tab(ipRange)
# +-------------+---------------+
# | reachable   | unreachable   |
# +=============+===============+
# | 192.168.0.1 | 192.168.0.2   |
# +-------------+---------------+
# |             | 192.168.0.3   |
# +-------------+---------------+
# |             | 192.168.0.4   |
# +-------------+---------------+
# |             | 192.168.0.5   |
# +-------------+---------------+
# |             | 192.168.0.6   |
# +-------------+---------------+