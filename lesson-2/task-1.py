# Реализовать скрипт для чтения/записи данных в формате csv

import csv
from pprint import pprint

with open("lesson-2/data-read.csv", "r") as file:
    reader = csv.reader(file)
    pprint(list(reader))

data = [
    ['field1', 'field2', 'field3', 'field4'],
    ['data1', 'data2', 'data3', 'data4'],
    ['data1', 'data2', 'data3', 'data4'],
    ['data1', 'data2', 'data3', 'data4'],
    ['data1', 'data2', 'data3', 'data4'],
    ['data1', 'data2', 'data3', 'data4']
]

with open("lesson-2/data-write.csv", "w") as file:
    file_writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    file_writer.writerows(data)