import re

pattern = r"www.([a-zA-Z0-9]+)((\-|\.)[a-zA-Z0-9]+)*(\.[a-zA-Z]+)\s*"

while True:
    text=input()
    if not text:
        break
    links= re.finditer(pattern, text)
    for link in links:
        print(link[0])



