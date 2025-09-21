"""
Utility functions for the Basics project.

This module contains common utility functions that can be used across the project.
"""

from typing import List, Union


def greet(name: str) -> str:
    """
    Generate a greeting message for a given name.
    
    Args:
        name: The name to greet
        
    Returns:
        A greeting message string
        
    Example:
        >>> greet("Alice")
        'Hello, Alice! Welcome to the Basics project!'
    """
    return f"Hello, {name}! Welcome to the Basics project!"


def calculate_average(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numbers to average
        
    Returns:
        The average of the input numbers
        
    Raises:
        ValueError: If the list is empty
        
    Example:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    
    return sum(numbers) / len(numbers)


def is_even(number: int) -> bool:
    """
    Check if a number is even.
    
    Args:
        number: The number to check
        
    Returns:
        True if the number is even, False otherwise
        
    Example:
        >>> is_even(4)
        True
        >>> is_even(5)
        False
    """
    return number % 2 == 0


def fibonacci(n: int) -> List[int]:
    """
    Generate the first n numbers in the Fibonacci sequence.
    
    Args:
        n: Number of Fibonacci numbers to generate
        
    Returns:
        List of the first n Fibonacci numbers
        
    Raises:
        ValueError: If n is negative
        
    Example:
        >>> fibonacci(5)
        [0, 1, 1, 2, 3]
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence