# Реализовать скрипт для преобразования данных в формате csv в формат yaml

import csv
import yaml
from pprint import pprint

with open("lesson-2/data-read.csv", "r") as file:
    reader = csv.reader(file)
    headers = next(reader)
    data = dict(zip(headers, reader))
    # print(headers)
    pprint(data)

with open("lesson-2/data-from-csv.yaml", "w") as file:
    yaml.dump(data, file)