# Реализовать скрипт для чтения/записи данных в формате yaml

import yaml
from pprint import pprint

with open("lesson-2/data-read.yaml", "r") as file:
    obj = yaml.load(file)
    pprint(obj)

field_list = ['field1', 'field2', 'field3']
data_list = ['data1', 'data2', 'data3']

data = { 'fields' : field_list, 'data' : data_list}

with open("lesson-2/data-write.yaml", "w") as file:
    yaml.dump(data, file)
