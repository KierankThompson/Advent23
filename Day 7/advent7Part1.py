tiebreaker = {"A":14,"K":13,"Q":12,"J":11,"T":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2,"1":1}
sortArr = []
s = open("advent7.txt","r")
s = s.readlines()
for i in s:
    sortArr.append((i.split()[0],i.split()[1]))
def sortbyHand(hand):
    arr = [0] * 14
    for card in hand:
        arr[tiebreaker[card]-1] += 1
    arr.sort(reverse=True)
    if arr[0] == 5:
        return 7
    elif arr[0] == 4:
        return 6
    elif arr[0] == 3 and arr[1] == 2:
        return 5
    elif arr[0] == 3:
        return 4
    elif arr[0] == 2 and arr[1] == 2:
        return 3
    elif arr[0] == 2:
        return 2
    else:
        return 1
sortArr.sort(key = lambda x:(sortbyHand(x[0]),tiebreaker[x[0][0]],tiebreaker[x[0][1]],tiebreaker[x[0][2]],tiebreaker[x[0][3]],tiebreaker[x[0][4]]))
ans = 0
for ind in range(len(sortArr)):
    ans += (ind+1) * int(sortArr[ind][1])
print(ans)

