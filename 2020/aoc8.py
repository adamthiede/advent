#!/usr/bin/env python3
lines=open("aoc8-input.txt")
rls=lines.readlines()
last=rls[-1]
itrls=iter(rls)

accumulator=0
#for line in itrls:
count=0
timescount=[0]*633
while count<len(rls):
    item=rls[count].strip().split(" ") 
    instruction=item[0]
    sign=item[1][:1]
    num=int(item[1])

    if timescount[count]>1:
        print(f"{count} {timescount[count]}: {instruction} and {sign} and {num} acc {accumulator}")
        break

    if instruction=="acc":
        count+=1
        accumulator+=num
    elif instruction=="nop":
        count+=1
    elif instruction=="jmp":
        count+=num
    else:
        print("error!")
        break

    timescount[count]+=1

print(f"{count} {timescount[count]}: {item}  acc {accumulator}")
lines.close()
