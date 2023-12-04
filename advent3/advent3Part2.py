s2 = open("advent3.txt","r")
s = s2.readlines()
dic = {}
directions = ((0, -1), (0, 1), (-1, 0), (1, 0),(1,1),(-1,-1),(1,-1),(-1,1))
ans = 0
counter = 0
for i in range(len(s)):
    lastNum = ""
    for j in range(len(s[i])):
        if s[i][j].isdigit():
            for d in directions:
                positionX = i+d[0]
                positionY = j+d[1]
                if 0 <= positionX < len(s) and 0 <= positionY < len(s[i]):
                    if not s[positionX][positionY].isdigit() and s[positionX][positionY] != "." and s[positionX][positionY] != "\n":
                        curDigit = s[i][j]
                        for mi in range(j-1,-1,-1):
                            if s[i][mi].isdigit():
                                curDigit = s[i][mi] + curDigit
                            else:
                                break
                        for ma in range(j+1,len(s[i])):
                            if s[i][ma].isdigit():
                                curDigit += s[i][ma] 
                            else:
                                break
                        if curDigit != lastNum:
                            if (positionX,positionY) not in dic:
                                dic.update({(positionX,positionY):(1,int(curDigit))})
                            else:
                                dic[(positionX,positionY)] +=  (int(curDigit),)
                            lastNum = curDigit
                            break
        else:
            lastNum = ""
for j in dic.values():
    ans2 = 1
    if len(j) >= 3:
        print(j)
        for l in j:
            ans2 *= l
    if ans2 != 1:   
        ans += ans2
print(ans)
        


            