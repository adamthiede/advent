#!/usr/bin/env python3
mine="shiny gold"
canhold=[]

def bagContains(bag):
    lines=open("aoc7-input.txt")
    rls=lines.readlines()
    last=rls[-1]
    itrls=iter(rls)
    temphold=[]
    for line in itrls:
        rep=line.replace("bags","bag")
        rep=rep.replace(".","")
        linearr=rep.strip().split(" contain ")
        for item in linearr:
            if bag in item:
                temphold.append(linearr[0])
    lines.close()
    if len(temphold) == 0:
        print("end")
        return 0
    else:
        for bag2 in temphold:
            print(f"recursing {bag2}")
            canhold.append(bag2)
            bagContains(bag2)
        return 0

#print(bagContains("shiny gold bag"))
def part2(bag):
    lines=open("aoc7-input.txt")
    rls=lines.readlines()
    last=rls[-1]
    itrls=iter(rls)
    temphold=[]
    for line in itrls:
        rep=line.replace("bags","bag")
        rep=rep.replace(" bag","")
        rep=rep.replace(".","")
        linearr=rep.strip().split(" contain ")
        if linearr[0] == "shiny gold":
            print(f"mybag: {linearr[0]} items: {linearr[1:]}")
            for item in linearr[1:]:
                num=item.split(" ")[0]
                print(num)

    lines.close()
 
part2(mine)

#print(seats)
print(f"count: {len(canhold)} arr: {canhold}")
