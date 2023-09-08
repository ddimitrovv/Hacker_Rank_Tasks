import re


def ten_digits_len_and_starts_with_789(input_string):
    pattern = r"^[789]\d{2}"
    return bool(re.match(pattern, input_string))


number_inputs = int(input())
for _ in range(number_inputs):
    current_number = input()
    print('YES' if ten_digits_len_and_starts_with_789(current_number) else 'NO')
