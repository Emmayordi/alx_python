def fibonacci_sequence(n):
    if n <= 0:
        return []  # Return an empty list for non-positive values of n

    # Initialize the Fibonacci sequence with the first two numbers
    sequence = [0, 1]

    # Generate the Fibonacci sequence up to the nth number
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence[:n]  # Return the first n numbers of the sequence


n = 10
result = fibonacci_sequence(n)
print(result)
