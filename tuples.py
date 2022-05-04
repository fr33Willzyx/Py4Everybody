name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split(' ')[6]
        hours = words.split(':')[0]
        if hours not in counts:
            counts[hours] = 1
        else :
            counts[hours] = counts[hours] + 1

for k,v in sorted(counts.items()):
    print (k,v)
