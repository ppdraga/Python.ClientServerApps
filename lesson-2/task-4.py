# Реализовать скрипт для преобразования данных в формате csv в формат json

import csv
import json
from pprint import pprint

with open("lesson-2/data-read.csv", "r") as file:
    reader = csv.reader(file)
    headers = next(reader)
    data = dict(zip(headers, reader))
    # print(headers)
    pprint(data)

with open("lesson-2/data-from-csv.json", "w") as file:
    json.dump(data, file, sort_keys=True , indent=2)