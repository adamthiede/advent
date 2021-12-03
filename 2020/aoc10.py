#!/usr/bin/env python3
lines=open("aoc10-input.txt")
rls=lines.readlines()
last=rls[-1]
#itrls=iter(rls)

nums=[]
for line in rls:
    nums.append(int(line.strip()))
print(nums)
nums.append(0)
nums.sort()
maxnum=max(nums)
nums.append(maxnum+3)

print(nums)
onediff=0
threediff=0
index=0
while index<len(nums)-1:
    if (nums[index+1]-nums[index]) == 1:
        onediff+=1
    elif (nums[index+1]-nums[index]) == 3:
        threediff+=1
    index+=1

print(f"nums has {len(nums)} items, 1d {onediff} 3d {threediff} full {onediff+threediff} should be len")
print(onediff*threediff)

lines.close()
