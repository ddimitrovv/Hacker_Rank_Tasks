def print_rangoli(size):
    import string

    alphabet = string.ascii_lowercase
    pattern = []

    for i in range(size):
        row = '-'.join(alphabet[i:size])
        pattern.append((row[::-1] + row[1:]).center(4 * size - 3, '-'))

    for i in range(size - 1, 0, -1):
        print(pattern[i])

    print(pattern[0])

    for i in range(1, size):
        print(pattern[i])

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
