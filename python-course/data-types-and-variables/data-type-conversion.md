# Converting Data Types in Python

# Converting Data Types in Python

Python provides several built-in functions to convert between different data types. This process is called "type conversion" or "type casting." Here's how to convert between common data types:

## Converting to Strings

```python
# Converting different types to strings
integer_to_string = str(42)          # "42"
float_to_string = str(3.14)          # "3.14"
boolean_to_string = str(True)        # "True"
list_to_string = str([1, 2, 3])      # "[1, 2, 3]"
```

## Converting to Numbers

### To Integers
```python
# Converting to integers
string_to_int = int("42")            # 42
float_to_int = int(3.99)             # 3 (truncates, doesn't round)
boolean_to_int = int(True)           # 1 (True becomes 1, False becomes 0)

# Using a different base
binary_to_int = int("1010", 2)       # 10 (base 2)
hex_to_int = int("1A", 16)           # 26 (base 16)
```

### To Floats
```python
# Converting to floating-point numbers
string_to_float = float("3.14")      # 3.14
int_to_float = float(42)             # 42.0
boolean_to_float = float(False)      # 0.0
```

## Converting to Boolean

```python
# Converting to boolean
bool(1)                              # True
bool(0)                              # False
bool(42)                             # True (any non-zero number is True)
bool("")                             # False (empty string is False)
bool("Hello")                        # True (non-empty string is True)
bool([])                             # False (empty list is False)
bool([1, 2])                         # True (non-empty list is True)
```

## Converting to Lists, Tuples, and Sets

```python
# Convert to list
tuple_to_list = list((1, 2, 3))      # [1, 2, 3]
string_to_list = list("hello")       # ['h', 'e', 'l', 'l', 'o']
set_to_list = list({1, 2, 3})        # [1, 2, 3]

# Convert to tuple
list_to_tuple = tuple([1, 2, 3])     # (1, 2, 3)
string_to_tuple = tuple("hello")     # ('h', 'e', 'l', 'l', 'o')

# Convert to set (removes duplicates)
list_to_set = set([1, 2, 2, 3, 3])   # {1, 2, 3}
string_to_set = set("hello")         # {'h', 'e', 'l', 'o'}
```

## Converting to Dictionary

```python
# Convert a list of tuples to dictionary
list_to_dict = dict([("name", "John"), ("age", 30)])  # {'name': 'John', 'age': 30}

# Convert two lists to dictionary using zip
keys = ["name", "age", "job"]
values = ["Alice", 25, "Engineer"]
lists_to_dict = dict(zip(keys, values))  # {'name': 'Alice', 'age': 25, 'job': 'Engineer'}
```

## Handling Conversion Errors

Type conversions can raise exceptions if the conversion isn't possible:

```python
try:
    int("hello")  # This will raise ValueError
except ValueError as e:
    print(f"Conversion error: {e}")  # "Conversion error: invalid literal for int() with base 10: 'hello'"
```

## Type Checking

To check the type of a variable:

```python
x = 42
isinstance(x, int)         # True
isinstance(x, (int, float))  # True (checks against multiple types)
type(x) == int             # True (less preferred than isinstance)
```

Type conversion is essential for data processing and ensuring your variables have the correct type for the operations you want to perform.
