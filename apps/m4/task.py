import os
import sys

from bs4 import BeautifulSoup

input_file = sys.argv[1]
file_extension = os.path.splitext(input_file)[1].lower()
flag = 0
if file_extension == '.html' or file_extension == '.htm':
    parser = 'html.parser'
elif file_extension == '.xml':
    parser = 'xml'
    flag = 1
else:
    sys.exit(1)

try:
    with open(input_file, 'r', encoding="utf-8") as file:
        soup = BeautifulSoup(file, parser)
except FileNotFoundError:
    print(f"Error: File {input_file} not found.")
    sys.exit(1)

for node in soup:
  print(node)