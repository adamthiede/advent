#!/usr/bin/env python3
f=open("3.txt")
lines=f.readlines()
text=lines[0]

def decode(x,pos):
    val=[]
    if (x==">"):
        val=[pos[0]+1,pos[1]]
    elif (x=="^"):
        val=[pos[0],pos[1]+1]
    elif (x=="<"):
        val=[pos[0]-1,pos[1]]
    elif (x=="v"):
        val=[pos[0],pos[1]-1]
    else:
        return None
    return val

def part1():
    index=0
    visited=[[0,0]]
    for x in text:
        pos=visited[index]
        print(pos)
        print(x)
        if (x==">"):
            visited.append([pos[0]+1,pos[1]])
        elif (x=="^"):
            visited.append([pos[0],pos[1]+1])
        elif (x=="<"):
            visited.append([pos[0]-1,pos[1]])
        elif (x=="v"):
            visited.append([pos[0],pos[1]-1])
        else:
            print("input: ",x," BAD!")
            exit
        index+=1

def part2():
    index=0
    i2=0
    i3=0
    human=[[0,0]]
    robo=[[0,0]]
    for x in text:
        if (i3%2 == 0):
            #human
            pos=human[index]
            print(pos)
            human.append(decode(x,pos))
            index+=1
        else:
            #robo
            pos=robo[i2]
            print(pos)
            robo.append(decode(x,pos))
            i2+=1
        i3+=1    
    print("Done with part 2!")

part2()
