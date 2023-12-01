

s = open("advent1.txt","r")

digits = set(["1","2","3","4","5","6","7","8","9","0"])
a = 0
for i in s:
    bot = 0
    top = len(i) - 1
    ans = ""
    while bot != -1 or top != -1:
        if i[bot] in digits and bot != -1:
            ans = i[bot] + ans
            bot = -1
        elif bot != -1:
            bot += 1
        if i[top] in digits and top != -1:
            ans += i[top]
            top = -1
        elif top != -1:
            top -= 1
    if ans:
        a += int(ans)
print(a)