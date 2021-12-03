#!/usr/bin/env python3
f=open("1.txt")
lines=f.readlines()
count=0
index=0
for char in lines[0]:
    if count==-1:
        print(f"basement at {index}")
    if char=="(":
        count+=1
    elif char==")":
        count-=1
    index+=1
print(count)
