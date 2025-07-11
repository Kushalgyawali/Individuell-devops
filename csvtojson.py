import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = []

    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    with open(json_file_path, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    csv_to_json("profiles1.csv", "data.json")