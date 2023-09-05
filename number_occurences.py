# from collections import deque
#
# input_numbers = deque([int(x) for x in input()])
#
# counter = 0
# current_num = input_numbers[0]
# output = []
#
# while input_numbers:
#     num = input_numbers.popleft()
#
#     if num != current_num:
#         output.append(f'({counter}, {current_num})')
#         current_num = num
#         counter = 1
#     else:
#         counter += 1
#
# output.append(f'({counter}, {current_num})')
#
# print(' '.join(output))

# ---------- Second solution ----------

from itertools import groupby

input_string = input()
output = []

for key, group in groupby(input_string, lambda x: int(x)):
    count = len(list(group))
    output.append(f'({count}, {key})')

print(' '.join(output))
