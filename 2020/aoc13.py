#!/usr/bin/env python3
lines=open("aoc13-input.txt")
rls=lines.readlines()
last=rls[-1]
llen=len(rls[1])-1
itrls=iter(rls)


def part1():
    mytime=int(rls[0])
    print(mytime)
    sched=rls[1].strip().split(",")
    print(sched)
    buses=[]
    for bus in sched:
        if bus.isnumeric():
            buses.append(int(bus))

    print(buses)

    lowmod=mytime
    lowbus=0
    for bus in buses:
        bustime=bus 
        while bustime<mytime:
            bustime+=bus
        bustime-=mytime
        if bustime<lowmod:
            lowmod=bustime
            lowbus=bus
        print(f"bustime {bustime}")
    print(lowbus)
    print(lowbus*lowmod)

def part2():
    sched=rls[1].strip().split(",")
    index=0
    while index<len(sched):
        bus=sched[index]
        if bus.isnumeric():
            print(index,bus)
            sched[index]=int(bus)
        index+=1
    print(sched)

#part1()
part2()
#end
lines.close()
