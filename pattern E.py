'''def print_E_pattern(height):
    width = height // 2 + 1

    # Print top horizontal line
    print('*' * width)

    # Print middle vertical line
    for _ in range(height - 2):
        print('*')

    # Print bottom horizontal line
    print('*' * width)

# Example usage:
height = int(input("Enter the height of E pattern: "))
print_E_pattern(height)'''
def print_e_pattern(n):
    for i in range(n):
        if i == 0 or i == n // 2 or i == n - 1:
            print("*" * (n - 1))
        else:
            print("*")

# Get user input for size of the pattern
size = int(input("Enter the size of the pattern: "))
print_e_pattern(size)
