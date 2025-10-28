import os
import sys

from bs4 import BeautifulSoup, SoupStrainer

input_file = sys.argv[1]
file_extension = os.path.splitext(input_file)[1].lower()
if file_extension == '.html' or file_extension == '.htm':
    parser = 'html.parser'
elif file_extension == '.xml':
    parser = 'xml'
else:
    sys.exit(1)

# Parse all tags with id
only_tags_with_id = SoupStrainer(id = True)

try:
    with open(input_file, 'r', encoding="utf-8") as file:
        soup = BeautifulSoup(file, parser, parse_only=only_tags_with_id)
except FileNotFoundError:
    print(f"Error: File {input_file} not found.")
    sys.exit(1)

for tag in soup.find_all(id =True):
    print(tag)