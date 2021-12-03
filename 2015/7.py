#!/usr/bin/env python
f=open("7.txt")
lines=f.readlines()
instructions=[]
for arr in lines:
    dims=arr.strip().split(" ")
    instructions.append(dims)

print(instructions)

