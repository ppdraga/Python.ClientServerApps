import json
from socket import socket
from argparse import ArgumentParser
from protocol import validate_request, make_response
from resolvers import resolve
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

try:

    sock = socket()
    sock.bind((default_config.get('host'), default_config.get('port'),))
    sock.listen(5)

    # print(f"Server  is up and running on {default_config.get('host')}:{default_config.get('port')}")
    logging.info(f"Server  is up and running on {default_config.get('host')}:{default_config.get('port')}")

    while True:
        client, address = sock.accept()
        # print(f'Client is connected on {address[0]}:{address[1]}')
        logging.info(f'Client is connected with {address[0]}:{address[1]}')
        # b_request = client.recv(default_config.get('buffersize'))
        # print(f'Client sent message: {b_request.decode()}')
        # client.send(b_request)
        b_request = client.recv(default_config.get('buffersize'))
        request = json.loads(b_request.decode())
        
        if validate_request(request):
            action_name = request.get('action')
            controller = resolve(action_name)
            if controller:
                try:
                    # print(f'Controller {action_name} resolved with request: {request}')
                    logging.debug(f'Controller {action_name} resolved with request: {request}')
                    response = controller(request)
                except Exception as err:
                    # print(f'Controller {action_name} error: {err}')
                    logging.critical(f'Controller {action_name} error: {err}')
                    response = make_response(request, 500, 'Internal server error')
            else:
                # print(f'Controller {action_name} not found')
                logging.error(f'Controller {action_name} not found')
                response = make_response(request, 404, f'Action with name {action_name} not supported')
        else:
            # print(f'Controller wrong request: {request}')
            logging.error(f'Controller wrong request: {request}')
            response = make_response(request, 400, 'wrong request format')

        client.send(
            json.dumps(response).encode()
        )
        client.close()

except KeyboardInterrupt:
    # print('Server terminated')
    logging.info('Server terminated')