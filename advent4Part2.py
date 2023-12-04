s = open("advent4.txt","r")
fans = 0
numArr = [1] * 214
numArr[0] = 0
for i in s:
    num = i.split(":")[0].split()[1]
    print(num)
    j = i.split(":")[1]
    k = j.split("|")
    l1 = k[0].split()
    l2 = k[1].split()
    setL = set()
    for m in l1:
        setL.add(m)
    ans = 0
    for n in l2:
        if n in setL:
            ans += 1
    for o in range(int(num)+1,int(num)+ans+1):
        numArr[o] += numArr[int(num)]
print(sum(numArr))
        
