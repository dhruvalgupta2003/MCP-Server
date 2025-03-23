def main():
	print('Hello from mcp!')


def sum_even_numbers(numbers: Iterable[int]) -> int:
	"""Given an iterable of integers, return the sum of all even numbers in the iterable."""
	return sum(num for num in numbers if num % 2 == 0)


def print_hello():
	for _i in range(19):
		print('hello')


if __name__ == '__main__':
	main()
