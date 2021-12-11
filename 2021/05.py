#!/usr/bin/env python3
f=open("05.txt")
lines=f.readlines()
arr=[]
for line in lines:
    filter1=line.strip().split(" -> ")
    filter2=list(map(int,filter1[0].split(",")))
    filter3=list(map(int,filter1[1].split(",")))
    filter4=filter2+filter3
    arr.append(filter4)

floorMap=[]
for x in range(0,1000):
    floorMap.append([0])
    for y in range(0,1000):
        floorMap[x].append(0)
        
def part1():
    overlaps=0
    print("part1")
    for i in arr:
        if i[0] == i[2]:
            print(f"we have a match on Xs. {i}")
            ys=[i[1],i[3]]
            for a in range(min(ys),max(ys)+1):
                floorMap[i[0]][a]+=1
        elif i[1] == i[3]:
            print(f"we have a match on Ys. {i}")
            xs=[i[0],i[2]]
            for a in range(min(xs),max(xs)+1):
                floorMap[a][i[1]]+=1
        else:
            print("ignore")
            #ignore
    #print(floorMap)
    for x in floorMap:
        for y in x:
            if y>1:
                overlaps+=1
    print(overlaps)

def part2():
    print("part2")

part1()
#part2()
