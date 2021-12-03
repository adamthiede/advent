#!/usr/bin/env python3
import os
import hashlib
#f=open("4.txt")
#lines=f.readlines()
#text=lines[0]
text='bgvyzdsv'
print(text)

def part1():
    print("begin part 1")
    for x in range(1,9000000000):
        concat=text+str(x)
        csum=hashlib.md5(concat.encode()).hexdigest()
        ff=csum[0:5]
        if ff == '00000':
            print("FOUND IT",csum,x)
            exit(0)
    print("end part 1")

def part2():
    print("begin part 2")
    print("end part 2")

part1()
#part2()
