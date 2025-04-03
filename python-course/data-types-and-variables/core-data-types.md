# Core Data Types in Python

# Core Data Types in Python

Python has several built-in data types that serve as the foundation for all Python programs. Here's an overview of the most important ones:

## Numeric Types

### Integers (`int`)
Whole numbers without a decimal point.

```python
age = 25
count = -10
big_number = 10000000000  # Python handles large integers automatically
```

### Floating-Point Numbers (`float`)
Numbers with a decimal point.

```python
pi = 3.14159
temperature = -2.5
scientific = 1.23e-4  # Scientific notation (0.000123)
```

### Complex Numbers (`complex`)
Numbers with a real and imaginary part.

```python
c = 3 + 4j  # Where j represents the imaginary unit
```

## Text Type

### Strings (`str`)
Sequences of characters, created with single or double quotes.

```python
name = "Alice"
message = 'Hello, World!'
multiline = """This string
spans multiple
lines"""

# String operations
greeting = "Hello, " + name  # Concatenation
repeat = "Echo " * 3         # Repetition: "Echo Echo Echo "
letter = name[0]             # Indexing: "A"
substring = name[1:3]        # Slicing: "li"
```

## Boolean Type

### Boolean (`bool`)
Represents truth values: either `True` or `False`.

```python
is_active = True
has_permission = False

# Boolean operations
result = is_active and has_permission  # False
another = is_active or has_permission  # True
opposite = not is_active               # False
```

## Sequence Types

### Lists (`list`)
Ordered, mutable collections of items.

```python
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", True, 3.14]

# List operations
fruits.append("orange")       # Add item
first_fruit = fruits[0]       # Access item
fruits[1] = "blueberry"       # Modify item
sliced = fruits[1:3]          # Get sublist
```

### Tuples (`tuple`)
Ordered, immutable collections of items.

```python
coordinates = (10, 20)
person = ("John", 25, "Developer")

# Tuple operations
x, y = coordinates            # Unpacking
name, age, job = person       # Multiple assignment
```

### Range (`range`)
Represents an immutable sequence of numbers.

```python
numbers = range(5)            # 0, 1, 2, 3, 4
even_numbers = range(2, 10, 2)  # 2, 4, 6, 8
```

## Mapping Type

### Dictionaries (`dict`)
Key-value pairs, unordered (though insertion order is preserved in Python 3.7+).

```python
person = {
    "name": "Alice",
    "age": 30,
    "is_student": False
}

# Dictionary operations
person["occupation"] = "Engineer"  # Add/modify item
name = person["name"]              # Access value by key
person.get("country", "Unknown")   # Access with default
```

## Set Types

### Sets (`set`)
Unordered collections of unique items.

```python
unique_numbers = {1, 2, 3, 3, 2, 1}  # Results in {1, 2, 3}

# Set operations
unique_numbers.add(4)               # Add item
is_present = 2 in unique_numbers    # Check membership
a = {1, 2, 3}
b = {3, 4, 5}
union = a | b                       # Union: {1, 2, 3, 4, 5}
intersection = a & b                # Intersection: {3}
```

### Frozen Sets (`frozenset`)
Immutable version of a set.

```python
immutable_set = frozenset([1, 2, 3])
```

## None Type

### None (`NoneType`)
Represents the absence of a value or a null value.

```python
result = None

def function_without_return():
    pass  # This function implicitly returns None
```

## Type Conversion

Python allows conversion between data types:

```python
# Converting between types
num_str = "42"
num = int(num_str)           # String to integer: 42
float_num = float(num)       # Integer to float: 42.0
back_to_str = str(num)       # Number to string: "42"
```

These core data types provide the building blocks for Python programming and understanding their properties and operations is essential for effective Python development.
