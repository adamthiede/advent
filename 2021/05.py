#!/usr/bin/env python3
f=open("05.txt")
lines=f.readlines()
arr=[]
for line in lines:
    arr.append(line.strip().split(" -> "))
print(arr)

def part1():
    print("part1")
    for i in arr:
        print(i[0], i[1])
        if (i[0][0] == i[1][0]) or (i[0][1] == i[1][1]):
            print("we have a match.")
        else:
            #ignore
            print("Ignored.")

def part2():
    print("part2")

part1()
#part2()
