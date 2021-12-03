#!/usr/bin/env python3
lines=open("aoc12-input.txt")
rls=lines.readlines()
last=rls[-1]
llen=len(rls[1])-1
itrls=iter(rls)

def turn(degrees, curdir, lorr):
    dirs=["N","E","S","W"]
    pos=dirs.index(curdir)
    turns=int(degrees/90)
    if lorr=="L":
        retval=dirs[(pos-turns)%len(dirs)]
    elif lorr=="R":
        retval=dirs[(pos+turns)%len(dirs)]
    print(f"turn {lorr} {degrees} from {curdir}, to {retval}")
    return retval

def part1():
    direction="E"
    ewpos=0
    nspos=0
    for line in rls:
        order=line.strip()
        letter=order[:1]
        number=int(order[1:])
        if letter=="F":
            # move forward
            if direction=="E":
                ewpos+=number
            elif direction=="W":
                ewpos-=number
            elif direction=="N":
                nspos+=number
            elif direction=="S":
                nspos-=number
        elif letter=="E":
            ewpos+=number
        elif letter=="W":
            ewpos-=number
        elif letter=="N":
            nspos+=number
        elif letter=="S":
            nspos-=number
        
        elif letter=="R" or letter=="L":
            direction=turn(number,direction, letter)
    aewpos=abs(ewpos)
    anspos=abs(nspos)
    print(aewpos+anspos)

def part2():
    direction="E"
    ewpos=0
    nspos=0
    wayew=10
    wayns=1
    for line in rls:
        order=line.strip()
        letter=order[:1]
        number=int(order[1:])
        if letter=="F":
            # move forward
            if direction=="E":
                ewpos+=number
            elif direction=="W":
                ewpos-=number
            elif direction=="N":
                nspos+=number
            elif direction=="S":
                nspos-=number
        elif letter=="E":
            ewpos+=number
        elif letter=="W":
            ewpos-=number
        elif letter=="N":
            nspos+=number
        elif letter=="S":
            nspos-=number
        
        elif letter=="R" or letter=="L":
            direction=turn(number,direction, letter)
    aewpos=abs(ewpos)
    anspos=abs(nspos)
    print(aewpos+anspos)

part2()

#end
lines.close()
