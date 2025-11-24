# Milestone-4: Iterable BeautifulSoup

## Overview

This milestone implements the functionality to make BeautifulSoup objects iterable. You can now directly iterate over BeautifulSoup objects using a `for` loop, which automatically traverses all nodes in the parse tree.

## Feature Description

### Implementation

The `__iter__` method was added to the `BeautifulSoup` class in `bs4/__init__.py`, making BeautifulSoup objects iterable.

```python
def __iter__(self) -> Iterator[PageElement]:
    yield from self.descendants
```

### How to use

```python
from bs4 import BeautifulSoup

html_doc = "<html><head><title>Test</title></head><body><p>Hello</p></body></html>"
soup = BeautifulSoup(html_doc, 'html.parser')

# Directly iterate over the soup object

for node in soup:
    print(node)

```

### Technical Details

1. **Iterator Implementation**: Iteration is implemented using the `descendants` property. This property returns all descendant nodes.

2. **Lazy Loading**: The iterator is lazy-loaded; not all nodes are pre-collected into a list. This ensures memory efficiency, especially for large documents.

3. **Traversal Order**: Iteration proceeds in document order, using the `next_element` pointer to traverse the entire tree structure.

4. **Node Types**: Iteration returns `PageElement` objects of all types, including:

- `Tag` objects (HTML/XML tags)

- `NavigableString` objects (text content)

- `Comment` objects (comments)

- Other `PageElement` subclasses

## Testing

Five unit tests are implemented in `bs4/tests/test_soup_iteration.py`:

```bash
cd bs4\tests
pytest test_soup_iteration.py
```

## File Structure

- **Implementation File**: `bs4/__init__.py` - Adds the `__iter__` method to the `BeautifulSoup` class.

- **Test File**: `bs4/tests/test_soup_iteration.py` - Contains 5 unit tests.

- **Documentation File**: `apps/m4/M4-README.md` - This technical documentation.

## Design Decisions

1. **Use `descendants`**: Choosing to use the existing `descendants` attribute instead of reimplementing the iteration logic allows for:

- Reusing existing, tested code

- Maintaining consistency with the existing API

2. **No Pre-collecting Nodes**: The implementation ensures that the iterator is lazy-loaded and does not pre-collect all nodes into the list, which is crucial for large documents.

3. **Maintaining Backward Compatibility**: The implementation does not affect the existing BeautifulSoup API; it only adds new iteration functionality.