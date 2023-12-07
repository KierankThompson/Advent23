import time
import copy
start = time.time()
s = open("advent5.txt","r")
mapping = [[] for _ in range(7)]
seeds = set()
s = s.readlines()
splitter = s[0][6:].split()
for i in range(0,len(splitter),2):
    seeds.add((int(splitter[i]),int(splitter[i+1])+int(splitter[i])))
print(seeds)
curIndex = 7
for j in range(1,len(s)):
    if s[j] == '\n':
        continue
    nums = s[j].split()
    try:
        dest = int(nums[0])
    except:
        curIndex -= 1
        continue
    loc = int(nums[1])
    spread = int(nums[2])
    #Check all the seeds for current value
    mapping[curIndex].append((dest,loc,spread))
findMin = 0
flag = False
for findMin in range(10000000):
    copyMin = findMin
    for map1 in mapping:
        for map2 in map1:
            if map2[0] <= copyMin < map2[0] + map2[2]:
                copyMin = copyMin - map2[0] + map2[1]
                break
    for check in seeds:
        if check[0] <= copyMin < check[1]:
            print(findMin)
            flag = True
    if flag == True:
        break
end = time.time()
print(end-start)

        

