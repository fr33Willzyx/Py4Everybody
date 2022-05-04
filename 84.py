fname = input("Enter file name: ")
fh = open(fname)
stuff = list()
for line in fh:
    words = line.split()
    for nword in words:
    	if nword in stuff: continue
        stuff.append(nword)
        stuff.sort()
print(stuff)
