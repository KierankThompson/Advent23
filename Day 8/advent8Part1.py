s = open("advent8.txt","r")
s = s.readlines()
mapDict = {}
directions = s[0]
for i in range(2,len(s)):
    mapDict.update({s[i][:3]:(s[i][7:10],s[i][12:15])})
curIndex = "AAA"
counter = 0
d = 0
while curIndex != "ZZZ":
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
print(counter)