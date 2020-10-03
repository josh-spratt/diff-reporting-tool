import csv
from deepdiff import DeepDiff
import json


def take_csv_and_create_dict(csv_path):
	new_dict = {}
	with open(csv_path, mode='r') as f:
		reader = csv.DictReader(f)
		for row in reader:
			key = row['first']+'-'+row['last']
			new_dict[key] = row
	return new_dict		


x = take_csv_and_create_dict('csv-1.csv')
y = take_csv_and_create_dict('csv-2.csv')


def diff_new_dicts(old_dict, new_dict):
	diff = DeepDiff(old_dict, new_dict)
	return diff


z = diff_new_dicts(x, y).to_dict()
print(z)

# print(json.dumps(z, indent=4))
# with open('csv-1.csv', mode='r') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         key = row['first']+'-'+row['last']
#         new_dict1[key] = row
# print(json.dumps(new_dict1, indent=4))

# with open('csv-2.csv', mode='r') as g:
#     reader = csv.DictReader(g)
#     for row in reader:
        

# x = DeepDiff(new_list2, new_list1)
# print(json.dumps(x, indent=4))
