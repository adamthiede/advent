#!/usr/bin/env python3
f=open("09.txt")
lines=f.readlines()
field=[]
points=[]
ct=0
for x in lines:
    field.append(x.strip())
    points.append([])
    for y in range(0,len(x.strip())):
        points[ct].append(0)
    ct+=1

print(len(field),len(field[0]))
print(len(points),len(points[0]))

def part1():
    totalsum=0
    for y in range(0,len(field)):
        for x in range(0,len(field[0])):
            mypoint=int(field[x][y])

            u=False
            d=False
            l=False
            r=False

            if y<1:
                u=True
            elif mypoint < int(field[x][y-1]):
                u=True

            if y>=len(field)-1:
                d=True
            elif mypoint < int(field[x][y+1]):
                d=True

            if x<1:
                l=True
            elif mypoint < int(field[x-1][y]):
                l=True

            if x>=len(field[0])-1:
                r=True
            elif mypoint < int(field[x+1][y]):
                r=True

            if u and d and l and r:
                # is a low point
                risk=1+int(field[x][y])
                print("low point.",mypoint,"at",x,y,risk)
                points[x][y]=risk
                totalsum+=risk
    print(totalsum)

def part2():
    print("part2")

part1()
part2()
