import os
import re

# Directory containing the log files
log_dir = "Server_Key_Logs"

# Function to extract sensitive information from log files
def extract_information(log_file):
    extracted_data = []
    
    # Regular expressions for common sensitive data patterns
    username_pattern = r"\b(?:user|username|login|email):?\s*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\b"
    password_pattern = r"\b(?:pass|password|pwd):?\s*([a-zA-Z0-9!@#$%^&*()_+=-]{6,})\b"
    credit_card_pattern = r"\b(?:\d{4}[- ]?){3}\d{4}\b"  # Basic pattern for credit card numbers

    try:
        with open(log_file, 'r') as file:
            for line in file:
                # Search for usernames and passwords in each line
                username_matches = re.findall(username_pattern, line, re.IGNORECASE)
                password_matches = re.findall(password_pattern, line, re.IGNORECASE)
                credit_card_matches = re.findall(credit_card_pattern, line)

                # Store the matches in the extracted data list
                if username_matches:
                    extracted_data.append(("Username", username_matches))
                if password_matches:
                    extracted_data.append(("Password", password_matches))
                if credit_card_matches:
                    extracted_data.append(("Credit Card", credit_card_matches))
    
    except Exception as e:
        print(f"Error reading {log_file}: {e}")

    return extracted_data

# Function to process all log files in the directory
def process_log_files():
    all_extracted_data = []

    # Iterate through each log file in the specified directory
    for filename in os.listdir(log_dir):
        if filename.endswith('.txt'):  # Process only text files
            print(filename)

            log_file_path = os.path.join(log_dir, filename)
            extracted_data = extract_information(log_file_path)
            if extracted_data:
                all_extracted_data.append((filename, extracted_data))
    
    return all_extracted_data

# Function to display the extracted information
def display_extracted_information(extracted_data):
    for filename, data in extracted_data:
        print(f"\nExtracted Information from {filename}:")
        for data_type, values in data:
            print(f"{data_type}: {', '.join(values)}")

if __name__ == "__main__":
    extracted_data = process_log_files()
    if extracted_data:
        display_extracted_information(extracted_data)
    else:
        print("No sensitive information found.")
