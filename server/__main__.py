import json
from socket import socket
from argparse import ArgumentParser


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

if args.config:
    with open(args.config) as file:
        file_config = json.load(file)
        default_config.update(file_config)


try:

    sock = socket()
    sock.bind((default_config.get('host'), default_config.get('port'),))
    sock.listen(5)

    print(f"Server  is up and running on {default_config.get('host')}:{default_config.get('port')}")

    while True:
        client, address = sock.accept()
        print(f'Client is connected on {address[0]}:{address[1]}')
        b_request = client.recv(default_config.get('buffersize'))
        print(f'Client sent message: {b_request.decode()}')
        client.send(b_request)
        client.close()

except KeyboardInterrupt:
    print('Server terminated')