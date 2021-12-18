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

# 7 segment display draw
draw={
    0:"abcefg",
    1:"cf",
    2:"acdeg",
    3:"acdfg",
    4:"bcdf",
    5:"abdfg",
    6:"abdefg",
    7:"acf",
    8:"abcdefg",
    9:"abcdfg"
}

# how many segments are 1, 4, 7, or 8
easy={
    2:1,
    4:4,
    3:7,
    7:8
}

def part1():
    ct=0
    print("part1")
    for i in a2:
        print(ct,i)
        for j in i:
            if len(j) in easy:
                ct+=1
    print(ct)

def part2():
    print("part2")

part1()
part2()
