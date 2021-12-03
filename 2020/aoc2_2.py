#!/usr/bin/env python3
f=open("input2.txt")
lines=f.readlines()
count=0
for line in lines:
    policy=line.split(" ")
    counts=policy[0].split("-")
    letter=policy[1][:1]
    pw=policy[2].strip()
    atone='' 
    attwo='' 
    atone=pw[int(counts[0])-1]
    attwo=pw[int(counts[1])-1]
    if(atone==letter and attwo==letter):
        print("both have letter, wrong")
    if(atone==letter and attwo!=letter):
        count+=1
    elif(atone!=letter and attwo==letter):
        count+=1
    #print(timesLetter)
    #print(counts,letter,pw)
    #print(f"Line: {line}")
print(f"{count} passwords are good")
