import re

# File paths
input_file = "extracted_data.txt"  # Replace with the path of the extracted data file
cleaned_file = "cleaned_data.txt"  # Desired output file path for cleaned data

def clean_data(input_file, cleaned_file):
    with open(input_file, "r") as infile, open(cleaned_file, "w") as outfile:
        clean_text = ""
        for line in infile:
            # Remove timestamp and event labels (e.g., "Pressed", "Released")
            match = re.search(r"- (Pressed|Released): (.+)", line)
            if match:
                key_event = match.group(2)
                
                # Check for printable keys
                if len(key_event) == 3 and key_event.startswith("'") and key_event.endswith("'"):
                    clean_text += key_event[1]  # Add the character (e.g., 'a')
                
                # Handle special key events like [Space] and [Enter]
                elif "[Space]" in key_event:
                    clean_text += " "
                elif "[Enter]" in key_event:
                    clean_text += "\n"
        
        # Write the cleaned text to the output file
        outfile.write(clean_text.strip())
        print(f"Data cleaning completed. Cleaned data saved in {cleaned_file}")

# Run the cleaning process
clean_data(input_file, cleaned_file)
