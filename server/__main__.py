import json
import select
from socket import socket
from argparse import ArgumentParser
from protocol import validate_request, make_response
from resolvers import resolve
from handlers import handle_default_request
import logging

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

# logger = logging.getLogger('main')
# logger.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# handler = logging.FileHandler('main.log')
# handler.setFormatter(formatter)
# handler.setLevel(logging.DEBUG)

# logger.addHandler(handler)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('main.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

requests = []
connections = []

try:
    sock = socket()
    sock.bind((default_config.get('host'), default_config.get('port'),))
    sock.settimeout(0)
    sock.listen(5)

    # print(f"Server  is up and running on {default_config.get('host')}:{default_config.get('port')}")
    logging.info(f"Server  is up and running on {default_config.get('host')}:{default_config.get('port')}")

    while True:
        try:
            client, address = sock.accept()
            connections.append(client)
            # print(f'Client is connected on {address[0]}:{address[1]}')
            logging.info(f'Client is connected with {address[0]}:{address[1]}')
        except:
            pass
        if len(connections) > 0:    
            rlist, wlist, xlist = select.select(
                connections, connections, connections, 0
            )
            for r_client in rlist:
                b_request = r_client.recv(default_config.get('buffersize'))
                requests.append(b_request)

            if requests:
                b_request = requests.pop()
                b_response = handle_default_request(b_request)

                for w_client in wlist:
                    w_client.send(b_response)

except KeyboardInterrupt:
    # print('Server terminated')
    logging.info('Server terminated')