import re
text=input()
pattern = r"\%([A-Z][a-z]+)\%\<([A-Z-a-z]+)\>[\w]*\|([\d]+)\|[A-Za-z\W]*([\d]+[\.\d]*)\$"
match = re.fullmatch(pattern, text)
print(match)