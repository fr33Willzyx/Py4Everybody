fname = input("Enter file name: ")
fh = open(fname)
count = 0
tval = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    pos = line.find("0")
    val = float(line[pos:])
    tval = tval + float(val)
print("Average spam confidence:", tval/count)
