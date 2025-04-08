
filled = int(input())
total = filled+2

db = []

for sq in range(filled):
    x,y = map(int,input().split())
    if x < total and y < total:
        if abs(x-y) > 1:
            for sqx in range(abs(x-y)):
                if not db.count((x+sqx,sq)): db.append((x+sqx,sq))
        else:
            if not db.count((x,sq)): db.append((x,sq))
    
mohit = 0
for x in range(total):
    for y in range(total):
        if db.count((x,y)):
            if not db.count((x+1,y)): mohit += 1
            if not db.count((x-1,y)): mohit += 1
            if not db.count((x,y+1)): mohit += 1
            if not db.count((x,y-1)): mohit += 1

print(mohit)