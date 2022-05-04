import re
hand = open('regexReal.txt')

numlist = list()
for line in hand:
    nums = re.findall('[0-9]+', line)
    if len(nums) < 1 : continue
    for num in nums:
        intnum = int(num)
        numlist.append(intnum)
print(sum(numlist))
