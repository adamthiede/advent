#!/usr/bin/env python3
#f=open("aoc3-input.txt")
lines=open("aoc3-input.txt")
#lines=f.readlines()
r3d1count=0
pos=0
llen=31
for line in lines:
    if(pos>=llen):
        pos=(pos%llen)
    display=line[:pos]+"@"+line[pos+1:]
    #print(line.strip())
    #print(display.strip())

    if(line[pos] == "#"):
        r3d1count+=1
    pos+=3
print(f"13count: {r3d1count}")
lines.close()
lines=open("aoc3-input.txt")

r1d1count=0
pos=0
for line in lines:
    if(pos>=llen):
        pos=(pos%llen)
    display=line[:pos]+"@"+line[pos+1:]
    #print(line.strip())
    #print(display.strip())

    if(line[pos] == "#"):
        r1d1count+=1
    pos+=1
print(f"11count: {r1d1count}")
lines.close()
lines=open("aoc3-input.txt")


r5d1count=0
pos=0
for line in lines:
    if(pos>=llen):
        pos=(pos%llen)
    display=line[:pos]+"@"+line[pos+1:]
    #print(line.strip())
    #print(display.strip())

    if(line[pos] == "#"):
        r5d1count+=1
    pos+=5
print(f"51count: {r5d1count}")
lines.close()
lines=open("aoc3-input.txt")


r7d1count=0
pos=0
for line in lines:
    if(pos>=llen):
        pos=(pos%llen)
    display=line[:pos]+"@"+line[pos+1:]
    #print(line.strip())
    #print(display.strip())

    if(line[pos] == "#"):
        r7d1count+=1
    pos+=7
print(f"71count: {r7d1count}")
lines.close()

lines=open("aoc3-input.txt")
rls=lines.readlines()
last=rls[-1]
itrls=iter(rls)
r1d2count=0
pos=0
for line in itrls:
    if(pos>=llen):
        pos=(pos%llen)
    display=line[:pos]+"@"+line[pos+1:]
    #print(line.strip())
    #print(display.strip())
    if(line[pos] == "#"):
        r1d2count+=1
    pos+=1
    if line is not last:
        next(itrls)
    
print(f"12count: {r1d2count}")
lines.close()

mult=r3d1count*r1d1count*r5d1count*r7d1count*r1d2count
print(f"multiplied: {mult}")
