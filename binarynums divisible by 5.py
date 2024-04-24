def binary_divisible_by_5(sequence):
    binary_numbers = sequence.split(',')
    result = []

    for binary_number in binary_numbers:
        decimal_number = int(binary_number, 2)
        if decimal_number % 5 == 0:
            result.append(binary_number)

    return ','.join(result)

input_sequence = input("Enter a sequence of comma-separated 4-digit binary numbers: ")
print("Numbers divisible by 5:", binary_divisible_by_5(input_sequence))