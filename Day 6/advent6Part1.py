s = open("advent6.txt","r")
s = s.readlines()
time = s[0][6:].split()
distance = s[1][10:].split()

finalAns = 1
for i in range(0,len(time)):
    ans = 0
    for j in range(1,int(time[i])):
        if j + int(distance[i]) / j <= int(time[i]):
            ans += 1
    finalAns *= ans
print(finalAns)


    