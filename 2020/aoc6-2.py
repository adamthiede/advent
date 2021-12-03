#!/usr/bin/env python3
lines=open("aoc6-input.txt")
rls=lines.readlines()
last=rls[-1]
itrls=iter(rls)

ans=[""]*26
answer=0
group=[]
germans=0
for line in itrls:
    if line != "\n":
        germans+=1
        for y in line.strip():
            group.append(y)

    elif line=="\n":
        print(f"people: {germans}\nfull {group}")
        groupuniq=list(dict.fromkeys(group))
        for l in groupuniq:
            if group.count(l) == germans:
                answer+=1
        print(f"answer: {answer}")
        group=[]
        germans=0

#print(seats)
print(f"people: {germans} answer: {answer}")
lines.close()
