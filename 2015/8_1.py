#!/usr/bin/env python
import re
f=open("8.txt")
lines=f.readlines()

def p1 ():
    l2=[]
    ct=0
    mct=0
    uct=0
    for line in lines:
        ct+=len(line)
        mod=line[1:len(line)-1]
        mod=str.encode(mod).decode()
        print(mod)
        if "\\\\" in mod:
            mod=mod.replace('\\\\','\\')
        if '\\"' in mod:
            mod=mod.replace('\\"','"')
        mct+=len(mod)

    print(f"count:{ct} mod:{mct} {ct-mct}")

def p2 ():
    print("part 2")

p1()
