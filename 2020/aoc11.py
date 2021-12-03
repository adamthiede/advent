#!/usr/bin/env python3
lines=open("aoc11-input.txt")
rls=lines.readlines()
last=rls[-1]
llen=len(rls[1])-1

seatmap=[]

for line in rls:
    row=[]
    for x in line.strip():
        row.append(x)
    seatmap.append(row)

def countOcc(row,index):
    occupied=0
    #check above
    if row!=0 and row!=98:
        if index!=0 and index!=llen:
            for x in range(index-1,index+2):
                print(f" check seat {row-1} {x} {seatmap[row-1][x]}")
                if seatmap[row-1][x]=="#":
                    print(f"seat {row-1} {x} {seatmap[row-1][x]} occupied!")
                    occupied+=1

    if occupied==0:
        print(f"occupying seat {row},{index}")

print(llen)
countOcc(3,3)

lines.close()
