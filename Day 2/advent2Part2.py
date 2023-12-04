s = open("advent2.txt","r")
ans = 0

nuhuh = set()
for i in s:
    i2 = i.split(":")
    maxR = 0
    maxG = 0
    maxB = 0
    for i3 in i2[1].split(";"):
        for i4 in i3.split(","):
            i5 = i4.split()
            if i5[1] == "green":
                maxG = max(maxG,int(i5[0]))
            elif i5[1] == "red":
                maxR = max(maxR,int(i5[0]))
            elif i5[1] == "blue":
                maxB = max(maxB,int(i5[0]))
    
    ans += maxR * maxG * maxB
print(ans)