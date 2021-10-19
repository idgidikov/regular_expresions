import re
pattern = r"(^|(?<=\s)(-*)(\d+)((\.\d+)*)($|(?=\s)))"
text = input()
matches = re.finditer(pattern,text)
