import re
total_income=0
while True:
    data= input()
    if data=="end of shift":
        break
    pattern=r"\%([A-Z][a-z]+)\%\<([A-Z-a-z]+)\>[\w]*\|([\d]+)\|[A-Za-z\W]*([\d]+[\.\d]*)\$"
    bar_income=re.finditer(pattern,data)
    for match in bar_income:
        quantity=match[3]
        price=match[4]
        total_price=float(quantity)*float(price)
        total_income+=total_price
        print(f"{match[1]}: {match[2]} - {total_price:.2f}")
print(f"Total income: {total_income:.2f}")


