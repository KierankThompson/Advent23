s = open("advent2.txt","r")
ans = 0
rMax = 12
gMax = 13
bMax = 14
nuhuh = set()
for i in s:
    i2 = i.split(":")
    for i3 in i2[1].split(";"):
        curR = 0
        curG = 0
        curB = 0
        for i4 in i3.split(","):
            i5 = i4.split()
            if i5[1] == "green":
                curG += int(i5[0])
            elif i5[1] == "red":
                curR += int(i5[0])
            elif i5[1] == "blue":
                curB += int(i5[0])
        if curR > rMax or curB > bMax or curG > gMax:
            nuhuh.add(int(i2[0].split()[1]))
    if int(i2[0].split()[1]) not in nuhuh:
        ans += int(i2[0].split()[1])
print(ans)