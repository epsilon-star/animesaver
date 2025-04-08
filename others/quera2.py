text = '14?100?1'
total = 1
lts = [int(x) for x in text.split('?')]
for x in range(len(lts)):
    if lts[x] == 1: continue
    elif lts[x+1] != 1:
        total *= lts[x]
    else:
        total *= lts[x]+lts[x+1]

print(total)