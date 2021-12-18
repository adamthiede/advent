#!/usr/bin/env python3
f=open("08.txt")
lines=f.readlines()
a1=[]
a2=[]
for line in lines:
    p1=line.split(" | ")[0].strip().split(" ")
    p2=line.split(" | ")[1].strip().split(" ")
    a1.append(p1)
    a2.append(p2)

print(a1[0]," | ",a2[0])

def part1():
    print("part1")

def part2():
    print("part2")

part1()
part2()
