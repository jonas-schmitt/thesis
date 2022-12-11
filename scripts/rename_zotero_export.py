# Import the required modules
import os

input_file = "bibliography"
output_file = f"{input_file}_fixed"
# Open the input file in read mode
with open(f'references/{input_file}.bib', 'r') as input_file:
    # Open the output file in write mode
    with open(f'references/{output_file}.bib', 'w') as output_file:
        # Write the processed line to the output file
        for line in input_file:
            if not "isbn" in line:
                output_file.write(line)
