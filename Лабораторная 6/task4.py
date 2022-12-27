import json
from typing import List

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename: str, delimiter: str = ",", new_line: str = '\n') -> List[dict]:
    '''
    Converts input .csv file into json
    '''
    data = []
    with open(filename) as f:
        headers = next(f).strip(new_line).split(delimiter)
        for line in f:
            lines = {header: li for header, li in zip(headers, line.strip(new_line).split(delimiter))}
            data.append(lines)
    return data

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))


