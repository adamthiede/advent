#!/usr/bin/env python3
f=open("2.txt")
lines=f.readlines()
total=0
rib=0
for arr in lines:
    dims=arr.split("x")
    l=int(dims[0])
    w=int(dims[1])
    h=int(dims[2].strip())
    area=(2*l*w)+(2*w*h)+(2*h*l)

    a2=[l, w, h]
    a2.remove(max(a2))
    area+=(a2[0]*a2[1])

    rib+=(sum(a2)*2)
    rib+=(l*w*h)

    print(dims, area)
    total+=area
    
print(total)
print("rib:",rib)
