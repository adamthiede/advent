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
    for y in range(0,len(field)-1):
        for x in range(0,len(field[0])-1):
            mypoint=int(field[x][y])
            if x==0 and y==len(field)-1:
                if mypoint < int(field[x][y-1]) and mypoint < int(field[x+1][y]):
                    risk=1+int(field[x][y])
                    print("low point.",mypoint,"at",x,y,risk)
                    points[x][y]=risk
                    totalsum+=risk
            if x==len(field)-1 and y==0:
                if mypoint < int(field[x][y+1]) and mypoint < int(field[x-1][y]):
                    risk=1+int(field[x][y])
                    print("low point.",mypoint,"at",x,y,risk)
                    points[x][y]=risk
                    totalsum+=risk
            if x==len(field)-1 and y==len(field)-1:
                if mypoint < int(field[x][y-1]) and mypoint < int(field[x-1][y]):
                    risk=1+int(field[x][y])
                    print("low point.",mypoint,"at",x,y,risk)
                    points[x][y]=risk
                    totalsum+=risk
            if x==0 and y==0:
                if mypoint < int(field[x][y+1]) and mypoint < int(field[x+1][y]):
                    risk=1+int(field[x][y])
                    print("low point.",mypoint,"at",x,y,risk)
                    points[x][y]=risk
                    totalsum+=risk
            if x<len(field)-1 and y<len(field)-1 and x>0 and y>0:
                # is in center of field
                if mypoint < int(field[x][y+1]) and mypoint < int(field[x][y-1]) and mypoint < int(field[x+1][y]) and mypoint < int(field[x-1][y]):
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
