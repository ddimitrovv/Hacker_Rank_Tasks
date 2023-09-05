input_string = input()
lowercase = sorted([x for x in input_string if x.islower()])
uppercase = sorted([x for x in input_string if  x.isupper()])
odd_digists = sorted([x for x in input_string if x.isdigit() and int(x) % 2 != 0])
even_digits = sorted([x for x in input_string if x.isdigit() and int(x) % 2 == 0])

output = f'{"".join(lowercase) + "".join(uppercase) + "".join(odd_digists) + "".join(even_digits)}'
print(output)
