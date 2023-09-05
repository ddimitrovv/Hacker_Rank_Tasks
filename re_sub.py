import re


n = int(input())
for _ in range(n):
    line = input()
    modified_line = re.sub(r'(?<= )&&(?= )|(?<= )\|\|(?= )',
                           lambda x: 'and' if x.group() == '&&' else 'or', line)
    print(modified_line)
