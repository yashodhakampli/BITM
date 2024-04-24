'''def print_x_pattern(name):
    length = len(name)
    for i in range(length):
        for j in range(length):
            if i == j or i + j == length - 1:
                print(name[j], end=' ')
            else:
                print(' ', end=' ')
        print()

name = "YASHODHA"
print_x_pattern(name)'''

'''def print_y_pattern(name):
    length = len(name)
    for i in range(length):
        for j in range(length):
            if i == j and i <= length // 2 or (i + j == length - 1 and i <= length // 2) or (j == length // 2 and i > length // 2):
                print(name[j], end=' ')
            else:
                print(' ', end=' ')
        print()

name = "YASHODHA"
print_y_pattern(name)'''

'''name = "yashodha"
rows = len(name) * 2 - 1
cols = len(name) * 2 - 1

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or i + j == rows - 1:
            print(name[j % len(name)], end="")
        else:
            print(" ", end="")
    print()'''

