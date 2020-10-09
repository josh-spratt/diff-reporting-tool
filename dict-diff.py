import csv
from deepdiff import DeepDiff
import json
import yaml


def take_csv_and_create_dict(csv_path):
    new_dict = {}
    with open(csv_path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = row['first'] + '-' + row['last']
            new_dict[key] = row
    return new_dict


old_data = take_csv_and_create_dict('csv-1.csv')
new_data = take_csv_and_create_dict('csv-2.csv')


def diff_new_dicts(old_dict, new_dict):
    diff = DeepDiff(old_dict, new_dict, ignore_order=True,
                    verbose_level=2).to_dict()
    return diff


final_diff = diff_new_dicts(old_data, new_data)


def write_output_yaml(diff_data):
    name = input('please name output file\n')
    with open('{0}.yaml'.format(name), 'w') as f:
        yaml.dump(diff_data, f)


write_output_yaml(final_diff)
