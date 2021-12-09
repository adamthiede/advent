#!/usr/bin/env python3
f=open("05.txt")
lines=f.readlines()
def part1():
    arr=[]
    for line in lines:
        arr.append(line.strip().split(" -> "))
    print("part1")
    print(int(arr[0][0].split(",")[0]))

def part2():
    print("part2")

part1()
part2()
