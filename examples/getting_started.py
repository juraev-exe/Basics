#!/usr/bin/env python3
"""
Getting Started Example

This script demonstrates how to use the basic utilities in our project.
Run this script to see the functions in action!
"""

import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import greet, calculate_average, is_even, fibonacci


def main():
    """
    Main function demonstrating the usage of our utility functions.
    """
    print("🎉 Welcome to the Basics Project!")
    print("=" * 50)
    
    # Demonstrate greet function
    print("\n1. Greeting Function:")
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        print(f"   {greet(name)}")
    
    # Demonstrate calculate_average function
    print("\n2. Average Calculator:")
    numbers_list = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [1.5, 2.5, 3.5, 4.5]
    ]
    
    for numbers in numbers_list:
        avg = calculate_average(numbers)
        print(f"   Average of {numbers} = {avg}")
    
    # Demonstrate is_even function
    print("\n3. Even Number Checker:")
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = [num for num in test_numbers if is_even(num)]
    odd_numbers = [num for num in test_numbers if not is_even(num)]
    
    print(f"   Even numbers: {even_numbers}")
    print(f"   Odd numbers: {odd_numbers}")
    
    # Demonstrate fibonacci function
    print("\n4. Fibonacci Sequence Generator:")
    fib_lengths = [5, 8, 10]
    
    for length in fib_lengths:
        fib_sequence = fibonacci(length)
        print(f"   First {length} Fibonacci numbers: {fib_sequence}")
    
    # Interactive section
    print("\n" + "=" * 50)
    print("🔧 Try it yourself!")
    print("Enter some numbers separated by spaces to calculate their average:")
    
    try:
        user_input = input("Numbers: ").strip()
        if user_input:
            user_numbers = [float(x) for x in user_input.split()]
            user_avg = calculate_average(user_numbers)
            print(f"Average of your numbers: {user_avg}")
            
            print(f"\nEven numbers from your input: {[num for num in user_numbers if num == int(num) and is_even(int(num))]}")
        else:
            print("No numbers entered!")
            
    except ValueError as e:
        print(f"Error: Please enter valid numbers. {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print("\n🎉 Thanks for trying our Basics project!")
    print("Check out the README.md and CONTRIBUTING.md for more information!")


if __name__ == "__main__":
    main()