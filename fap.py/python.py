def process_input(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.read().strip().split('\n')
    
    # Accumulate processed lines
    processed_lines = []
    current_entry = []
    
    for line in lines:
        if line.strip():  # If the line is not empty
            current_entry.append(line.strip())
        else:
            if current_entry:
                # Join all non-empty lines in the current entry and add to the processed list
                processed_lines.append('#'.join(current_entry))
                current_entry = []  # Reset for the next entry
    
    # Handle the last entry if there's no trailing newline in the file
    if current_entry:
        processed_lines.append('-'.join(current_entry))
    
    # Write processed lines to output file
    with open(output_file, 'w') as file:
        for line in processed_lines:
            file.write(line + '\n')

# File paths (adjust paths as necessary)
input_file_path = 'C:/Users/omalomo3/Desktop/Hypefind Audit/fap.py/input.txt'
output_file_path = 'C:/Users/omalomo3/Desktop/Hypefind Audit/fap.py/Output.txt'

# Call the function
process_input(input_file_path, output_file_path)
