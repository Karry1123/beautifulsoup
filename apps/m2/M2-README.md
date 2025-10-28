# Milestone 2

## Answer for Part 2
### API being used in Milestone 1:
   - BeautifulSoup.__init__
   - BeautifulSoup.prettify
   - Tag.__init__
   - Tag.get
   - Tag.find_all
   - Tag.find_parent
   - Tag.__setitem__
   - Tag.clear
### API being used in Milestone 2 part 1 additionally:
   - SoupStrainer.__init__
### API Locations (Original Source)
- **BeautifulSoup.__init__**: `beautifulsoup/bs4/__init__.py`, line 209
- **BeautifulSoup.prettify**: `beautifulsoup/bs4/element.py`, line 2601
- **Tag.__init__**: `beautifulsoup/bs4/element.py` : line 1569
- **Tag.get**: `beautifulsoup/bs4/element.py`, line 2160
- **Tag.find_all**: `beautifulsoup/bs4/element.py`, line 2715
- **Tag.find_parent**: `beautifulsoup/bs4/element.py`, line 992
- **Tag.__setitem__**: `beautifulsoup/bs4/element.py`, line 2223
- **Tag.clear**: `beautifulsoup/bs4/element.py`, line 2093
- **SoupStrainer.__init__**: `beautifulsoup/bs4/filter.py`, line 313

## Milestone Structure

```
beautifulSoup/~
├apps/
├── m2/
│   ├── task2.py              # Task from part-1
│   ├── task3.py              
│   ├── task4.py              
│   ├── task6.py              # Using new API SoupReplacer
│   ├── M2-README.md          # Answer part-2 and part-3
├bs4/
├── builder/
│   ├── _htmlparser.py        # Modify for SoupReplacer, task from part-3
│   ├── _lxml.py              # Modify for SoupReplacer, task from part-3
├── tests/
│   ├── test_soupreplacer.py  # Test file for SoupReplacer, task from part-3
├── __init__.py               # Modify for SoupReplacer, task from part-3
├── SoupReplacer.py           # Create a new API SoupReplacer, task from part-3
```

## How to Run
Navigate to m2:
```bash
cd apps/m2
```
### task2.py:

```bash
python task2.py your_file
```
### task3.py:

```bash
python task3.py your_file
```
### task4.py:

```bash
python task4.py your_file
```
### task6.py:

```bash
python task6.py your_file
```
### test_soupreplacer.py:
Navigate to tests 
```bash
cd bs4/tests
test_soupreplacer.py pytest