s = open("advent5.txt","r")
unique = set()
seeds = {}
s = s.readlines()
#Get starting values
for i in s[0][6:].split():
    seeds.update({int(i):int(i)})
for j in range(1,len(s)):
    #If string is equal to new line character then we enter a new mapping
    if s[j] == '\n':
        #Reset the unqiue set because we are in a new mapping
        unique.clear()
        continue
    nums = s[j].split()
    try:
        l1 = int(nums[0])
    except:
        continue
    l2 = int(nums[1])
    l3 = int(nums[2])
    #Check all the seeds for current value
    for iter in seeds:
        #Check if map location is between the smallest and largest possible value and not done before
        if l2 <= seeds[iter] < l2+l3 and iter not in unique:
            #Get the enumerator value + the map value
            seeds[iter] = seeds[iter] - l2 + l1
            #make sure we can't update this map until next rotation
            unique.add(iter)
minL = 10000000000000000
for findMin in seeds.values():
    minL = min(minL,findMin)
print(minL)

        
        
        

