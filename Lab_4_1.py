import json
from pathlib import Path

def task() -> float:
    file_name = "input.json"
    with open(file_name) as f:
        json_data = json.load(f)

    sum_values = sum([item["score"] * item["weight"] for item in json_data])
    return round(sum_values, 3)


if __name__ == "__main__":
    print(task())