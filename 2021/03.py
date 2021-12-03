#!/usr/bin/env python3
f=open("03.txt")
lines=f.readlines()
vals=[]
for x in lines:
    vals.append(x.strip())

def part1():
    gr=''
    er=''
    #print(int(vals[0],2),vals[0])
    for v in range(0,12):
        zero=0
        one=0
        for z in vals:
            if int(z[v])==0:
                zero+=1
            elif int(z[v])==1:
                one+=1
        if zero>one:
            gr+='0'
            er+='1'
        elif one>zero:
            gr+='1'
            er+='0'
        else:
            gr+='?'
            er+='?'
    print(f"gr {gr}, er {er}")
    print("gr decimal: ",int(gr,2),"er decimal: ",int(er,2))
    print(int(gr,2)*int(er,2))


def part2():
    print("part2")

part1()
part2()
