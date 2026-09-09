sl = []

while True:
    s = input()
    if s == '': break
    sl.append(s)

r = []

for s in sl:
    if s.isupper() and s.len() > 4:
        r.append(s)

print(r)