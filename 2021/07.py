#!/usr/bin/env python3
f=open("07.txt")
lines=f.readlines()
arr=list(map(int,lines[0].split(",")))

def part1():
    print("part1")
    arrMin=min(arr)
    arrMax=max(arr)
    print(arrMin,arrMax)
    sel=arrMin
    totalUsed=[]
    for i in range(arrMin,arrMax):
        myFuel=0
        for x in arr:
            myFuel+=abs(x-i)
        print(myFuel)
        totalUsed.append(myFuel)
    print(min(totalUsed))

def part2():
    print("part2")
    arrMin=min(arr)
    arrMax=max(arr)
    print(arrMin,arrMax)
    sel=arrMin
    totalUsed=[]
    for i in range(arrMin,arrMax):
        myFuel=0
        for x in arr:
            for a in range(1,abs(x-i)+1):
                myFuel+=a
            #myFuel+=abs(x-i)
#        print(myFuel)
        print(i)
        totalUsed.append(myFuel)
    print(min(totalUsed))



#part1()
part2()
