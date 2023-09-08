import re

pattern = r'^[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

n = int(input())

for _ in range(n):
    line = input()
    name, email = re.findall(r'([^<]+) <([^>]+)>', line)[0]
    if re.match(pattern, email):
        print(f'{name} <{email}>')
