# Basic Input and Output in Python

# Basic Input and Output in Python

Python provides simple built-in functions for interacting with users through the console: `print()` for output and `input()` for input.

## The `print()` Function

`print()` displays information to the console.

### Basic Usage

```python
print("Hello, World!")  # Displays: Hello, World!

name = "Alice"
print("Hello,", name)   # Displays: Hello, Alice
```

### Multiple Arguments

```python
age = 30
print("Name:", name, "Age:", age)  # Displays: Name: Alice Age: 30
```

### Formatting Options

```python
# Using f-strings (Python 3.6+)
print(f"Hello, {name}! You are {age} years old.")

# Using .format()
print("Hello, {}! You are {} years old.".format(name, age))

# Specifying formatting for numbers
price = 49.9999
print(f"Price: ${price:.2f}")  # Displays: Price: $50.00
```

### Controlling End Characters

By default, `print()` adds a newline at the end:

```python
# Changing the end character
print("Hello", end=" ")
print("World")  # Displays: Hello World

# Using other end characters
print("Loading", end="...")
print("Done")  # Displays: Loading...Done
```

### Redirecting Output

```python
# Send output to a file
with open("output.txt", "w") as f:
    print("This goes to the file", file=f)
```

## The `input()` Function

`input()` reads text from the console and returns it as a string.

### Basic Usage

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

When this code runs:
1. It displays: `Enter your name: `
2. Waits for the user to type and press Enter
3. Stores the entered text in the `name` variable

### Converting Input to Other Types

Since `input()` always returns a string, you need to convert it to use it as another type:

```python
# Getting a number from the user
age_str = input("Enter your age: ")
age = int(age_str)  # Convert to integer

# Or in one line
age = int(input("Enter your age: "))

# Getting a floating-point number
height = float(input("Enter your height in meters: "))
```

### Input Validation

Always handle potential errors when converting user input:

```python
try:
    age = int(input("Enter your age: "))
    if age < 0:
        print("Age cannot be negative!")
    else:
        print(f"You are {age} years old.")
except ValueError:
    print("Please enter a valid number for age.")
```

## Combining Input and Output

A complete example showing both in action:

```python
print("Welcome to the Temperature Converter")
print("-" * 35)  # Prints a separator line

# Get temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display result
print(f"{celsius}°C is equivalent to {fahrenheit:.1f}°F")
print("Thank you for using the converter!")
```

This simple input/output system forms the foundation for user interaction in Python programs, especially when you're learning and creating basic command-line applications.
