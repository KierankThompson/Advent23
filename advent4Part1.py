s = open("advent4.txt","r")
fans = 0
for i in s:
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
    if ans > 0:
        fans += 2**(ans-1)
print(fans)
        
