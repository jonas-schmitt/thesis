# Import the required modules
import os

input_file = "zotero_export"
output_file = f"{input_file}_fixed"
# Open the input file in read mode
with open(f'references/{input_file}.bib', 'r') as input_file:
    # Open the output file in write mode
    with open(f'references/{output_file}.bib', 'w') as output_file:
        # Read each line of the input file
        for line in input_file:
            # Process the line
            if("@" in line):
                tmp1 = line.split("{")
                tmp2 = tmp1[1].split(",")
                tmp3 = tmp2[0].split("_")
                if("-" in tmp3[1]):
                    tmp = tmp3[1].split("-")
                    tmp3[1] = tmp[0]
                new_line = f"{tmp1[0]}{{{tmp3[0]}{tmp3[2]}{tmp3[1]},\n"
            else:
                new_line = line
            
            # Write the processed line to the output file
            if not "file =" in new_line and "keywords =" not in new_line:
                output_file.write(new_line)