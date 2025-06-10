from pathlib import Path
import re

def format_as_code_block(my_list: list) -> list:
    '''Adds back-ticks to each item in a list'''
    for i, item in enumerate(my_list):
        my_list[i] = f'`{item}`'

# Set up directories
root_dir = Path(__file__).parent
input_dir = root_dir / 'input_files'
output_dir = root_dir / 'output_files'

# Regex patterns to search
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
website_pattern = r'https?://[^\s]+|www\.[^\s]+|(?<!@)\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'

# Iterate through input directory
for file in input_dir.iterdir():
    with open(file) as f:
        print(f'Reading {file.name}...')
        text = f.read()

        # Search results
        emails_found = re.findall(email_pattern, text)
        phones_found = re.findall(phone_pattern, text)
        websites_found = re.findall(website_pattern, text)

        if emails_found:
            print(f'Emails found: {emails_found}')
            format_as_code_block(emails_found)

        if phones_found:
            print(f'Phones found: {phones_found}')
            format_as_code_block(phones_found)
        
        if websites_found:
            print(f'Websites found: {websites_found}')
            format_as_code_block(websites_found)

        # NEED TO RE-WRITE FILE AND SAVE INTO OUTPUT DIRECTORY
