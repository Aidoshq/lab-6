fn = input()
l = []
with open(fn, 'r') as f:
    for line in f:
        l.append(line)
print(l)
