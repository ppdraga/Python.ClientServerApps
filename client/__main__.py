import json
from socket import socket
from argparse import ArgumentParser
from datetime import datetime
import logging
import hashlib

parser = ArgumentParser()

parser.add_argument(
    '-c', '--config', type=str,
    required=False, help='Sets config file path'
)

args = parser.parse_args()

default_config = {
    'host': 'localhost',
    'port': 7777,
    'buffersize': 1024
}

# logger = logging.getLogger('main')
# logger.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# handler = logging.FileHandler('client.log')
# handler.setFormatter(formatter)
# handler.setLevel(logging.DEBUG)

# logger.addHandler(handler)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('client.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

if args.config:
    with open(args.config) as file:
        file_config = json.load(file)
        default_config.update(file_config)

sock = socket()
sock.connect(
    (
        default_config.get('host'), 
        default_config.get('port')
    )
)

print(f'Client is up and running')
logging.info(f'Client is up and running')

hash_obj = hashlib.sha256()
hash_obj.update(
    str(datetime.now().timestamp()).encode()
)

action = input('Enter action: ')
data = input('Enter data: ')
request = {
    'action': action,
    'time': datetime.now().timestamp(),
    'data': data,
    'token': hash_obj.hexdigest()
}

s_request = json.dumps(request)

sock.send(s_request.encode())
# print(f'Client sent data: {data}')
logging.info(f'Client sent data: {data}')
b_response = sock.recv(default_config.get('buffersize'))
print(b_response.decode())