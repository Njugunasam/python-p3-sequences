#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = [0, 1]

    for _ in range(2, length):
        other_number = sequence[-1] + sequence[-2]
        sequence.append(other_number)

    print(sequence[:length])
