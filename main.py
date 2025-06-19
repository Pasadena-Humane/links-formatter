from pathlib import Path
import re

def format_as_code_block(patterns: list, text: str) -> str:
    '''Adds back-ticks to each item in a list'''
    for pattern in patterns:
        text = re.sub(pattern, r'`\g<0>`', text)
    return text

# Set up directories
root_dir = Path(__file__).parent
input_dir = root_dir / 'input_files'
output_dir = root_dir / 'output_files'

patterns = [
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # emails
    r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}(?:\s*x\s*\d+)?',   # phones with optional extensions
    r'(?<!\]\()(https?://[^\s\)]+/?|www\.[^\s\)]+/?|(?<!@)\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s\)]*)?/?)\b(?!\))'  # websites/URLs excluding markdown links
]

# Iterate through input directory
for file in input_dir.iterdir():
    if file.is_file():
        print(f'Processing {file.name}...')

        text = file.read_text()
        for pattern in patterns:
            matches_found = re.findall(pattern, text)
            print(f'Matches found: {matches_found}')

        formatted_text = format_as_code_block(patterns, text)

        # Check for trailing forward slashes
        if '`/' in formatted_text:
            formatted_text = formatted_text.replace('`/', '/`')
            
        new_file = output_dir / file.name
        new_file.write_text(formatted_text)        
        print(f'Formatted matches as code blocks!')
