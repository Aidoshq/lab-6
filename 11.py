import string
for l in string.ascii_letters:
    fd = open(l + ".txt", "w")
    fd.close()