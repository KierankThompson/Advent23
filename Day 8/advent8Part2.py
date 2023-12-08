from math import gcd
s = open("advent8.txt","r")
s = s.readlines()
mapDict = {}
directions = s[0]
for i in range(2,len(s)):
    mapDict.update({s[i][:3]:(s[i][7:10],s[i][12:15])})

a2z = []
for a in mapDict:
    if a[2]  != 'A':
        continue
    curIndex = a
    counter = 0
    d = 0
    while curIndex[2] != "Z":
        if directions[d] == "R":
            curIndex = mapDict[curIndex][1]
            counter += 1
        elif directions[d] == "L":
            curIndex = mapDict[curIndex][0]
            counter += 1
        if d >= len(directions)-1:
            d = 0
        else:
            d += 1
    a2z.append(counter)
lcm = 1
for i in a2z:
    lcm = i*lcm//gcd(i,lcm)
print(lcm)