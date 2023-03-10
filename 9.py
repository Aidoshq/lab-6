fn = input()
cntl = 0
with open(fn, 'r') as f:
    for line in f:
        cntl += 1
print(cntl)