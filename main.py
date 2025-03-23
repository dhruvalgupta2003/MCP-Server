from collections.abc import Iterable


def main():
    print("Hello from MCP!")  # Double quotes instead of single (style issue)


def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers."""
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
        else:
            pass  # Unnecessary 'pass' statement (F)
    return total


def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers and return the result."""
    return a * b


def print_hello():
    for _ in range(5):
        print("hello")  # Double quotes instead of single (style issue)


if __name__ == "__main__":
    main()
