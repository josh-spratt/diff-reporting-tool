import csv
from deepdiff import DeepDiff
import json

new_list1 = []
new_list2 = []

with open('csv-1.csv', mode='r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        new_list1.append(row)

with open('csv-2.csv', mode='r') as g:
    reader = csv.DictReader(g)
    for row in reader:
        new_list2.append(row)

# print(new_list1)
# print(new_list2)

x = DeepDiff(new_list2, new_list1)
print(json.dumps(x, indent=4))
