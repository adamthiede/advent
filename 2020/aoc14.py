#!/usr/bin/env python3
lines=open("aoc14-input.txt")
rls=lines.readlines()
last=rls[-1]
llen=len(rls[1])-1
itrls=iter(rls)

count=0

def part1():
    for line in rls:
        if line.contains("mask:"):
            
        print(line.strip())
    print(f"part1: {count}")

def part2():
    print(f"part2: {count}")

part1()
#part2()
#end
lines.close()
