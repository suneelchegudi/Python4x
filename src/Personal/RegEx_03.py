import re
pattern = r"\W"
str = "Hello, Suneel !"

matches = re.findall(pattern, str)

print(matches)

result = re.split("\s",str)
print(result)

d = "ABCDEFGH"
print(d[:3])
