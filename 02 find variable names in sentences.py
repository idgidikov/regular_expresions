import re
pattern =r"\b_([a-zA-Z0-9]+)\b"
text = input()
#matches= re.findall(pattern,text)
matches=re.finditer(pattern,text)
all_variable_names = []
for match in matches:
    all_variable_names.append(match[1])


print(",".join(all_variable_names))


