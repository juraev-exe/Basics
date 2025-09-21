# API Reference

This document provides detailed information about all functions and classes in the Basics project.

## utils.py

### greet(name: str) -> str

Generate a greeting message for a given name.

**Parameters:**
- `name` (str): The name to greet

**Returns:**
- `str`: A greeting message string

**Example:**
```python
from src.utils import greet
message = greet("Alice")
print(message)  # Output: Hello, Alice! Welcome to the Basics project!
```

### calculate_average(numbers: List[Union[int, float]]) -> float

Calculate the average of a list of numbers.

**Parameters:**
- `numbers` (List[Union[int, float]]): List of numbers to average

**Returns:**
- `float`: The average of the input numbers

**Raises:**
- `ValueError`: If the list is empty

**Example:**
```python
from src.utils import calculate_average
avg = calculate_average([1, 2, 3, 4, 5])
print(avg)  # Output: 3.0
```

### is_even(number: int) -> bool

Check if a number is even.

**Parameters:**
- `number` (int): The number to check

**Returns:**
- `bool`: True if the number is even, False otherwise

**Example:**
```python
from src.utils import is_even
print(is_even(4))  # Output: True
print(is_even(5))  # Output: False
```

### fibonacci(n: int) -> List[int]

Generate the first n numbers in the Fibonacci sequence.

**Parameters:**
- `n` (int): Number of Fibonacci numbers to generate

**Returns:**
- `List[int]`: List of the first n Fibonacci numbers

**Raises:**
- `ValueError`: If n is negative

**Example:**
```python
from src.utils import fibonacci
fib = fibonacci(5)
print(fib)  # Output: [0, 1, 1, 2, 3]
```