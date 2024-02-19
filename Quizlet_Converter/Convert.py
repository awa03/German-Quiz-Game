
import os
import sys
import json

def convert_to_json(input_file, output_directory, output_filename):
    # Read data from the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Process each line to extract German word and its definition
    data = []
    for line in lines:
        if line.strip():  # Check if the line is not empty
            german, definition = line.strip().split(',', 1)
            entry = {"Word": german.strip(), "Definition": definition.strip()}
            data.append(entry)

    # Convert data to JSON format
    json_data = json.dumps(data, ensure_ascii=False, indent=4)

    # Construct the output file path
    output_file = os.path.join(output_directory, output_filename)

    # Write JSON data to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(json_data)

    print("Conversion completed successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py input_file output_directory output_filename")
        sys.exit(1)

    input_file = sys.argv[1]
    output_directory = "../Windows/Study_Set/"
    output_filename = sys.argv[2]

    convert_to_json(input_file, output_directory, output_filename)
