name = input("Enter file:")
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split(' ')[1]
        if words not in counts:
            counts[words] = 1
        else :
            counts[words] = counts[words] + 1

bigword = None
bigcount = None
for words,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = words
        bigcount = count

print(bigword,bigcount)
