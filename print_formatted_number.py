def print_formatted(number):
    width_decimal = len(str(number))
    width_octal = len(oct(number)[2:])
    width_hexadecimal = len(hex(number)[2:])
    width_binary = len(bin(number)[2:])

    for i in range(1, number + 1):
        decimal_str = str(i)
        octal_str = oct(i)[2:]
        hexadecimal_str = hex(i)[2:].upper()
        binary_str = bin(i)[2:]

        print(f"{decimal_str.rjust(width_binary)} {octal_str.rjust(width_binary)} {hexadecimal_str.rjust(width_binary)} {binary_str.rjust(width_binary)}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)