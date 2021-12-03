#!/usr/bin/env python3
f=open("input2.txt")
lines=f.readlines()
count=0
for line in lines:
    policy=line.split(" ")
    counts=policy[0].split("-")
    letter=policy[1][:1]
    pw=policy[2].strip()
    
    timesLetter=pw.count(letter)
    if(timesLetter>=int(counts[0]) and timesLetter<=int(counts[1])):
        count+=1
        print(policy)
    #print(timesLetter)
    #print(counts,letter,pw)
    #print(f"Line: {line}")
print(f"{count} passwords are good")
