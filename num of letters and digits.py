def count_letters_and_digits(input_string):
    num_letters = 0
    num_digits = 0
    for char in input_string:
        if char.isalpha():
            num_letters += 1
        elif char.isdigit():
            num_digits += 1
    return num_letters, num_digits

# Example usage:
input_string = input("Enter a string: ")
letters, digits = count_letters_and_digits(input_string)
print("Number of letters:", letters)
print("Number of digits:", digits)