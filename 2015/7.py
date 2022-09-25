#!/usr/bin/env python
def threeop(a, op, b):
    if op=="AND":
        return a & b
    elif op=="OR":
        return a | b
    elif op=="LSHIFT":
        return a << b
    elif op=="RSHIFT":
        return a >> b
    elif op=="OR":
        return a ^ b
def twoop(op, a):
    if op=="AND":
        return a & b
    elif op=="OR":
        return a | b
    elif op=="LSHIFT":
        return a << b
    elif op=="RSHIFT":
        return a >> b
    elif op=="OR":
        return a ^ b


def translate(x):
    op=''
    if len(x)==3:
        return threeop(x[0],x[1],x[2])
    elif len(x)==2:
        op=x[0]



def part1():
    f=open("7.txt")
    lines=f.readlines()
    f.close()
    values={}
    ops=['AND','OR','LSHIFT','RSHIFT','NOT']
    for arr in lines:
        dims=arr.strip().split(" -> ")
        left=dims[0].split(" ")
        right=dims[1]
        # eval left
        if op[0].isnumeric():
            op[0]=int(op[0])
        else:
            values[op[0]]=int(op[0])

        if len(op)==3:
            values[dims[1]]=translate(op)


    #print(values)

part1()
