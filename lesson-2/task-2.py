# Реализовать скрипт для чтения/записи данных в формате json

import json
from pprint import pprint

with open("lesson-2/data-read.json", "r") as file:
    obj = json.load(file)
    pprint(obj)

data = {
    'field1': 'data1',
    'field2': 'data2',
    'field3': 'data3',
    'field4': 'data4',
    'field5': {
        'subf1': 'subd1', 
        'subf2': 'subd2', 
        'subf3': 'subd3'
        },
    'field6': 'data6'
    }

with open("lesson-2/data-write.json", "w") as file:
    json.dump(data, file, sort_keys=True , indent=2)
