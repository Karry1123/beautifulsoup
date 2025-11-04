import os
import sys

from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer

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

replacer = SoupReplacer(attrs_xformer=lambda tag:{**tag.attrs, "class": "test"} if tag.name == "p" else tag.attrs)

try:
    with open(input_file, 'r', encoding="utf-8") as file:
        soup = BeautifulSoup(file, parser, replacer=replacer)
except FileNotFoundError:
    print(f"Error: File {input_file} not found.")
    sys.exit(1)

if flag == 0:
    if '.' in input_file:
        output_file = input_file.rsplit('.', 1)[0] + "_pretty.html"
    else:
        output_file = input_file + "_pretty.html"
else:
    if '.' in input_file:
        output_file = input_file.rsplit('.', 1)[0] + "_pretty.xml"
    else:
        output_file = input_file + "_pretty.xml"

with open(output_file, 'w', encoding="utf-8") as file:
    file.write(soup.prettify())

print(f"Output written to {output_file}")