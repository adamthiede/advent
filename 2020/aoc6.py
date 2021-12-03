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
        for y in line.strip():
            germans+=1
            group.append(y)

    elif line=="\n":
        print(f"full {group}")
        groupuniq=list(dict.fromkeys(group))
        print(f"nodup {groupuniq}")
        answer+=(len(groupuniq))
        group=[]
        germans=0

#print(seats)
print(f"sum: {answer}")
lines.close()
