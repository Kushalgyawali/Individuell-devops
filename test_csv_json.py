import csv
import json

def test_csv_column_count():
    with open("profiles1.csv", newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        assert len(header) == 12

def test_csv_row_count():
    with open("profiles1.csv", newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        rows = list(reader)
        assert len(rows) >= 900

def test_json_structure():
    with open("data.json", encoding='utf-8') as f:
        data = json.load(f)
        keys = data[0].keys()
        assert "firstname" in keys
        assert "lastname" in keys

def test_json_row_count():
    with open("data.json", encoding='utf-8') as f:
        data = json.load(f)
        assert len(data) >= 900
