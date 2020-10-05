import csv
from deepdiff import DeepDiff
import json


def take_csv_and_create_dict(csv_path):
    new_dict = {}
    with open(csv_path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = row['first'] + '-' + row['last']
            new_dict[key] = row
    return new_dict


x = take_csv_and_create_dict('csv-1.csv')
y = take_csv_and_create_dict('csv-2.csv')


def diff_new_dicts(old_dict, new_dict):
    diff = DeepDiff(old_dict, new_dict, ignore_order=True, verbose_level=2).to_dict()
    return diff


z = diff_new_dicts(x, y)
