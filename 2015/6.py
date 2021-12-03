#!/usr/bin/env python3
f=open("6.txt")
lines=f.readlines()
instructions=[]
for arr in lines:
    dims=arr.strip().split(" ")
    if dims[0]=="turn":
        dims.pop(0)
    instructions.append(dims)

# initialize the grid, no touch
grid=[]
for x in range(0,1000):
    grid.append([])
    for y in range(0,1000):
        grid[x].append(0)
# grid init done

for l in instructions:
    if l[0]=='on':
        #print(f"on {l[1]}\t{l[3]}")
        c1=l[1].split(",")
        c2=l[3].split(",")
        x1=int(c1[0])
        y1=int(c1[1])
        x2=int(c2[0])
        y2=int(c2[1])
        for a in range(x1,x2+1):
            for b in range(y1,y2+1):
                grid[a][b]=1
    elif l[0]=='off':
        #print(f"of {l[1]}\t{l[3]}")
        c1=l[1].split(",")
        c2=l[3].split(",")
        x1=int(c1[0])
        y1=int(c1[1])
        x2=int(c2[0])
        y2=int(c2[1])
        for a in range(x1,x2+1):
            for b in range(y1,y2+1):
                grid[a][b]=0
    elif l[0]=='toggle':
        #print(f"tg {l[1]}\t{l[3]}")
        c1=l[1].split(",")
        c2=l[3].split(",")
        x1=int(c1[0])
        y1=int(c1[1])
        x2=int(c2[0])
        y2=int(c2[1])
        for a in range(x1,x2+1):
            for b in range(y1,y2+1):
                if (grid[a][b]==0):
                    grid[a][b]=1
                elif (grid[a][b]==1):
                    grid[a][b]=0
    else:
        print("huh?")

other=0
for x in range(0,1000):
    for y in range(0,1000):
        if grid[x][y]==1:
            other+=1
print(other)
