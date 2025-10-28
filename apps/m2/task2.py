import os
import sys

from bs4 import BeautifulSoup
from bs4.filter import SoupStrainer

input_file = sys.argv[1]
file_extension = os.path.splitext(input_file)[1].lower()
if file_extension == '.html' or file_extension == '.htm':
    parser = 'html.parser'
elif file_extension == '.xml':
    parser = 'xml'
else:
    sys.exit(1)

# Parse only <a> tags
only_a_tags = SoupStrainer("a")

try:
    with open(input_file, 'r', encoding="utf-8") as file:
        soup = BeautifulSoup(file, parser, parse_only=only_a_tags)
except FileNotFoundError:
    print(f"Error: File {input_file} not found.")
    sys.exit(1)

for hyper in soup.find_all("a"):
    href = hyper.get('href')
    if href:
        print(href)