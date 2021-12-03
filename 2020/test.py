#!/usr/bin/env python3
f=open("aoc3-input.txt")
#lines=f.readlines()
for line in f:
    print(line.strip())
    next_line=f.readline()
    if(next_line):
        print("next")
