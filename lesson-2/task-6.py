# Реализовать скрипт для преобразования данных в формате json в формат yaml

import json
import yaml
from pprint import pprint

with open("lesson-2/data-read.json", "r") as file:
    data = json.load(file)
    pprint(data)

with open("lesson-2/data-from-json.yaml", "w") as file:
    yaml.dump(data, file)