# Milestone-3
**SoupReplacer Evolution — Technical Brief**  
A Proposal to the BeautifulSoup Core Team  

**Author**: Zian Xu
**Date**: 2025-11-04  

---

## 1. Current State

| Milestone | API Shape                            | Typical Usage                              |
|-----------|--------------------------------------|--------------------------------------------|
| **M2**    | `SoupReplacer(og_tag, alt_tag)`      | `SoupReplacer("b", "strong")`              |
| **M3**    | `SoupReplacer(name_xformer=, attrs_xformer=, xformer=)` | Functional callbacks |

---

## 2. Side-by-Side Comparison

| Dimension       | Milestone 2                     | Milestone 3                                      | Winner |
|-----------------|---------------------------------|--------------------------------------------------|--------|
| **Flexibility** | Global 1-to-1 mapping only     | Arbitrary conditions, attrs, side-effects        | M3     |
| **Learning Curve** | Zero lambdas                 | One lambda does it all                           | M3     |
| **Runtime Cost** | O(1) dict lookup               | O(1) call + tiny DummyTag                        | Tie    |
| **Backward Compatibility** | 100%                        | Fully backward-compatible                        | Tie    |
| **Debuggability** | Obvious pair                  | `print` inside lambda                            | M3     |

---

## 3. Why Merge M3 into Mainline?

1. **Real-World Demand**  
   The three most requested HTML-cleanup jobs are:  
   - Tag normalization (`b` → `strong`)  
   - Class cleanup / renaming  
   - Attribute injection / removal  
   M3 solves all three in a single line.

2. **Zero-Friction Migration**  
   ```python
   # M2
   SoupReplacer("font", "span")
   # M3 (exact same effect)
   SoupReplacer(name_xformer=lambda t: "span" if t.name=="font" else t.name)
   
## Milestone Structure

```
beautifulSoup/~
├apps/
├── m3/            
│   ├── task7.py              # Using new API SoupReplacer
│   ├── M3-README.md          # A small technical brief
├bs4/
├── builder/
│   ├── _htmlparser.py        # Modify for SoupReplacer, task from milestone-3
│   ├── _lxml.py              # Modify for SoupReplacer, task from milestone-3
├── tests/
│   ├── test_soupreplacer.py  # Update test file for SoupReplacer, task from milestone-3
├── __init__.py               # Modify for new SoupReplacer, task from milestone-3
├── SoupReplacer.py           # Update SoupReplacer, task from milestone-3
```

## How to Run
Navigate to m3:
```bash
cd apps/m3
```
### task7.py:

```bash
python task7.py your_file
```
### test_soupreplacer.py:
Navigate to tests 
```bash
cd bs4/tests
test_soupreplacer.py pytest
```