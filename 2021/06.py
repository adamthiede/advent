#!/usr/bin/env python3
f=open("06.txt")
lines=f.readlines()
fish_str=lines[0].strip().split(",")
fish=list(map(int,fish_str))
print(fish)

def spawnFish(fishList,day):
    if day>0:
        newList=[]
        for i in range(0,len(fishList)):
            if fishList[i]==0:
                fishList[i]=6
                newList.append(8)
            else:
                fishList[i]-=1
        day-=1
        fishList+=newList
        print(f"finished day {day}")
        spawnFish(fishList,day)
    else:
        print(len(fishList))
        print("all done!")


def part1():
    print("part1")
    finalArr=spawnFish(fish,80)
    print(finalArr)
    print(len(finalArr))


def part2():
    print("part2")
    finalArr=spawnFish(fish,256)

#part1()
part2()
