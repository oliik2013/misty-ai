import csv
import json
import sys

csv.field_size_limit(10_000_000)

def convert_csv_to_dataset(input_path: str, output_path: str):
    dataset = []

    with open(input_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            message = row.get('message', '').strip()
            response = row.get('response', '').strip()
            if message and response:
                dataset.append({
                    "input": message,
                    "output": response
                })

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)

    print(f"Done — {len(dataset)} entries written to {output_path}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python csv_to_dataset.py <input.csv> <output.json>")
        sys.exit(1)

    convert_csv_to_dataset(sys.argv[1], sys.argv[2])
