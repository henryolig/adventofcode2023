
# Part 1

fp = open('input.txt')
lines = fp.readlines()
found_parts = []
i1 = 0
lines = list(map(lambda x: x.strip(), lines))
newmat = []
for line in lines:
    newmat.append(line.split('.'))
for i in newmat:
    print(i)


fp.close()