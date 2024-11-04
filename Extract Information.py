import re

# File paths
input_file = "S:\\Programms\\PYTHON\\KeyLogger\\Server_Key_Logs\\server_keylog_20241102_172353.txt"  # Replace with your input log file
output_file = "extracted_data.txt"  # Replace with the desired output file for extracted data

def extract_data(input_file, output_file):
    previous_char = None  # Track the last written character to avoid duplicates
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            # Match lines with only alphanumeric keys or space
            match = re.search(r"(Pressed|Released):\s*'(\w)'", line)
            if match:
                current_char = match.group(2)
                # Write the character only if it differs from the previous one
                if current_char != previous_char:
                    outfile.write(current_char)
                    previous_char = current_char
            # Match lines with space or enter special keys
            elif "Released: [Space]" in line:
                if previous_char != " ":
                    outfile.write(" ")
                    previous_char = " "
            elif "Released: [Enter]" in line:
                if previous_char != "\n":
                    outfile.write("\n")
                    previous_char = "\n"
    print(f"Data extraction completed. Extracted data saved in {output_file}")

# Run the extraction
extract_data(input_file, output_file)
