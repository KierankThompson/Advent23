

s = open("advent1.txt","r")

digits = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9","zero":"0"}
a = 0
for i in s:
    ans = ""
    rans = ""
    lans = ""
    rindex = -1
    lindex = -1
    for j in digits:
        l = i.find(j)
        r = i.rfind(j)
        if l != -1:
            if lindex == -1:
                lindex = l
                lans = j
            elif lindex > l:
                lindex = l
                lans = j
        if r != -1:
            if rindex < r:
                rindex = r
                rans = j
    bot = 0
    top = len(i) - 1
    topD = 0
    botD = 0
    while botD != -1 or topD != -1:
        if i[bot] in digits.values() and botD != -1:
            botD = -1
        elif botD != -1:
            bot += 1
        if i[top] in digits.values() and topD != -1:
            topD = -1
        elif topD != -1:
            top -= 1
    if lindex == -1 or bot < lindex:
        ans += i[bot]
    elif lindex < bot:
        ans += digits[lans]
    if rindex == -1 or top > rindex:
        ans += i[top]
    elif rindex > top:
        ans += digits[rans]
    if ans:
        a += int(ans)
        
print(a)