# Python Comments

Python offers several ways to add comments to your code. Comments are ignored by the Python interpreter but are extremely valuable for humans reading your code.

## Single-line Comments

The most common type of comment starts with the hash symbol (`#`). Everything after this symbol on the same line is considered a comment:

```python
# This is a single-line comment
x = 5  # This comment is at the end of a line of code
```

## Multi-line Comments

Python doesn't have a specific syntax for multi-line comments like some other languages do. However, there are two common approaches:

### 1. Using Multiple Single-line Comments

```python
# This is the first line of a comment
# This is the second line
# And this is the third line
```

### 2. Using Triple Quotes (Docstrings)

Although technically not comments but string literals, triple quotes are often used for multi-line text that is ignored during execution:

```python
"""
This is a multi-line comment using triple quotes.
It can span multiple lines.
And is often used for documentation.
"""

# Code continues here
```

Triple-quoted strings that appear at the beginning of a module, function, class, or method are called "docstrings" and are used for documentation.

## Best Practices for Python Comments

1. **Be Clear and Concise**: Write comments that explain "why" rather than "what"

2. **Update Comments**: Keep comments updated when you change your code

3. **Docstrings**: Use docstrings for modules, classes, and functions:

```python
def calculate_area(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius (float): The radius of the circle
        
    Returns:
        float: The area of the circle
    """
    return 3.14159 * (radius ** 2)
```

4. **Comment Complex Logic**: Focus comments on parts of code that might be difficult to understand

5. **Avoid Obvious Comments**: Don't comment things that are already clear from the code

6. **Use Comments for TODOs**:

```python
# TODO: Implement error handling for network timeouts
```

Good comments make your code more maintainable and help other developers (including future you) understand your thought process when writing the code.
