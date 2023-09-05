input_string = input()
lowercase = [x for x in input_string if x.islower()]
uppercase = [x for x in input_string if  x.isupper()]
odd_digists = [x for x in input_string if x.isdigit() and int(x) % 2 != 0]
even_digits = [x for x in input_string if x.isdigit() and int(x) % 2 == 0]

output = f'{"".join(sorted(lowercase)) + "".join(sorted(uppercase)) + "".join(sorted(odd_digists)) + "".join(even_digits)}'
print(output)
