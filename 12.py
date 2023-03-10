rd = open('rawdata.txt', 'r')
wt = open('data.txt', 'w')
for line in rd:
    wt.write(line)