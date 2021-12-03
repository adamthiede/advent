#!/usr/bin/env python3
lines=open("aoc9-input.txt")
rls=lines.readlines()
last=rls[-1]
itrls=iter(rls)

nums=[]
for line in rls:
    nums.append(int(line.strip()))
pre=nums[:25]
index=25
invalid=0
for val in nums[25:]:
    found=0
    for x in pre:
        if x <= val and found==0:
            for y in pre:
                if (x+y)==val:
                    found=1
    index+=1
    pre=nums[(index-25):index]
    if found==0:
        invalid=val
        print(f"found is 0 on {val}")
        break

print(invalid)
tig=[]
for n in nums:
    if n < invalid:tig.append(n)

i=0
weak=[]
while i<len(tig)-1:
    current=tig[i]
    j=i+1
    weak.append(tig[i])
    while j<len(tig) and current<=invalid:
        current+=tig[j]
        weak.append(tig[j])
        if(current==invalid):
            print("Got here!")
            print(f"{i} {j} {current}")
            print(sum(weak))
            minw=min(weak)
            maxw=max(weak)
            print(f"{minw} {maxw} {minw+maxw}")
            break
        j+=1
    i+=1
    weak=[]

lines.close()
