#!/usr/bin/env python3
f=open("02.txt")
lines=f.readlines()
def part1():
    print("part1")
    location=[0,0]
    for line in lines:
        direction=line.split(" ")[0].strip()
        number=int(line.split(" ")[1].strip())
        if direction=="forward":
            location[0]+=number
        elif direction=="up":
            location[1]-=number
        elif direction=="down":
            location[1]+=number
        #print(f"{direction} {number}")
    print(location)
    print(location[0]*location[1])

def part2():
    print("part2")
    location=[0,0,0]
    for line in lines:
        direction=line.split(" ")[0].strip()
        number=int(line.split(" ")[1].strip())
        if direction=="forward":
            location[0]+=number
            location[1]+=(number*location[2])
        elif direction=="up":
            location[2]-=number
        elif direction=="down":
            location[2]+=number
        #print(f"{direction} {number}")
    print(location)
    print(location[0]*location[1])


part1()
part2()
