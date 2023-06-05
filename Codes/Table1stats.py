ma, mi = 0,11110000
lc, wc, wcc = 0, 0,0
with open('Datasets/Dengue.txt','r') as f:
    for line in f:
        lc += 1
        line1 = (" ".join(line))
        wc += len(line1.strip().split())
        wcc =len(line1.strip().split())
        if wcc > ma:
            ma= wcc
        if wcc < mi:
            mi = wcc
avg = wc / lc

print('Total genome sequences are:', lc)
print('Total bases are:', wc)
print('Minimum Sequence length is:', mi)
print('Maximum Sequence Length is: ',ma)
print('Average sequence length is:', avg)

##############tablestats#############
