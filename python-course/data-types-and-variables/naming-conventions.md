# Python Naming Conventions

# Python Naming Conventions

Python has established naming conventions defined in PEP 8 (Python Enhancement Proposal 8), the official style guide. Following these conventions makes your code more readable and consistent with the Python ecosystem.

## General Rules

- Names should be descriptive and meaningful
- Avoid single-letter names except for counters or iterators
- Avoid using reserved keywords (like `list`, `str`, `type`, etc.)

## Specific Conventions

### Variables and Functions

- Use lowercase with underscores (snake_case):
```python
user_name = "John"
item_count = 42

def calculate_total(price, quantity):
    return price * quantity
```

### Classes

- Use CapWords/CamelCase (start each word with uppercase, no underscores):
```python
class Student:
    pass

class DatabaseConnection:
    pass
```

### Constants

- Use uppercase with underscores:
```python
MAX_CONNECTIONS = 100
PI = 3.14159
DEFAULT_CONFIG_PATH = "/etc/app/config"
```

### Modules

- Use short, all-lowercase names
- Can use underscores if it improves readability:
```python
# Filename: data_processor.py
import data_processor
```

### Packages

- Use short, all-lowercase names
- Preferably without underscores:
```python
import numpy
from matplotlib import pyplot
```

## Special Conventions

### Private Variables/Methods

- Prefix with a single underscore for "internal use" indication (weak "private" hint):
```python
_internal_variable = "Not meant for direct access"

def _helper_function():
    pass
```

### "Private" Class Members

- Prefix with double underscore for name mangling (stronger privacy hint):
```python
class Person:
    def __init__(self):
        self.__secret = "Hidden attribute"  # Will be transformed to _Person__secret
```

### Magic Methods

- Surrounded by double underscores:
```python
class Sample:
    def __init__(self):
        pass
    
    def __str__(self):
        return "Sample object"
```

### Non-Public API

- Use a single trailing underscore for names that conflict with Python keywords:
```python
class_ = "Physics 101"
def_ = "Definition"
```

## Recommendations for Variables

- **Loop variables**: It's acceptable to use single-letter names (commonly `i`, `j`, `k`):
```python
for i in range(10):
    print(i)
```

- **Boolean variables**: Often prefixed with `is_`, `has_`, `can_`:
```python
is_active = True
has_permission = False
can_edit = True
```

Following these conventions helps make your code more maintainable and easier for other Python developers to understand.
