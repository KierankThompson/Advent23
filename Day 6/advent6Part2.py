
s = open("advent6.txt","r")
s = s.readlines()
time = ""
for t in s[0][6:].split():
    time += t
distance = ""
for d in s[1][10:].split():
    distance += d
ans = 0
for j in range(1,int(time)):
    if j + int(distance) / j <= int(time):
        ans += 1
print(ans)

    