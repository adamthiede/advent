#!/usr/bin/env python3
f=open("01.txt")
lines=f.readlines()
def part1():
    prev=0
    count=0
    for x in lines:
        if int(x)>prev:
            count+=1
        prev=int(x)
    
    print(count-1)
def part2():
    s=[]
    for x in lines:
        s.append(int(x))
    i=0
    prev=0
    count=0
    for i in range(0,len(s)-2):
        a=s[i]+s[i+1]+s[i+2]
        if a > prev:
            count+=1
        prev=a
        print(i,count)
    print(f"count {count}, count-1 {count-1}")
part2()
