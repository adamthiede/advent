#!/usr/bin/env python3
f=open("5.txt")
lines=f.readlines()

def vow(word):
    ct=0
    vowels=["a","e","i","o","u"] 
    for v in vowels:
        ct+=word.count(v)
    if ct>=3:
        return True
    else:
        return False

def continuous(word):
    for x in range(0,len(word)-1):
        if word[x]==word[x+1]:
            return True
    return False

def banned(word):
    blacklist=["ab", "cd", "pq", "xy"]
    for item in blacklist:
        if word.find(item)!=-1:
            return False
    return True

def p2cont(word):
    for x in range(0,len(word)-2):
        tw=word[x:x+2]
        if word.find(tw) != word.rfind(tw) and abs(word.find(tw)-word.rfind(tw))>=2:
            print(f"Hey! {tw} {word}")
            return True
    return False

def p2bet(word):
    betct=0
    for c in range(0,len(word)-2):
        if word[c]==word[c+2]:
            betct+=1
    if betct>=1:
        return True
    else:
        return False

def part1():
    part1ct=0
    for line in lines:
        if vow(line) and continuous(line) and banned(line):
            part1ct+=1
            print(line)
    print(f"amt is {part1ct}")

def part2():
    print("part2")
    part2ct=0
    for line in lines:
        if p2cont(line) and p2bet(line):
            part2ct+=1
            print(line)
    print(f"amt is {part2ct}")

#part1()
part2()
