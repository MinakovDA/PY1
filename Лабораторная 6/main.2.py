import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file) -> list[dict]:
    list = []
    with open(file, 'r', encoding='utf-8') as f:
        keys_string = f.readline()
        keys = keys_string.rstrip('\n').split(',')
        for values_string in f.readlines():
            values = values_string.rstrip('\n').split(',')
            list.append(dict(zip(keys, values)))
        return list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
