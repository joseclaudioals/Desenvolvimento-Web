t = ((1,2), (3, 4), (5,6))
l = [list(item) for item in t]
for li in l:
    li[1] = li[1] + 10

print(l)