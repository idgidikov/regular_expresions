import re
racers=input().split(", ")
stats={}
while True:
    data = input()
    if data =="end of race":
        break
    pattern_racer = r"[a-zA-Z]+"
    miles_pattern=r"[0-9]"
    racer= re.findall(pattern_racer, data)
    miles = re.findall(miles_pattern, data)
    name=("".join(racer))
    miles=list(map(int,miles))
    if name in racers:
        if name not in stats:
            stats[name]=sum(miles)
        else:
            stats[name]+=sum(miles)
sorted_stats = dict(sorted(stats.items(),key=lambda x: -x[1]))
print(f"1st place: {tuple(sorted_stats.items())[0][0]}\n2nd place: {tuple(sorted_stats.items())[1][0]}\n3rd place: {tuple(sorted_stats.items())[2][0]}")