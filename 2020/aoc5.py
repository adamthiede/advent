#!/usr/bin/env python3
lines=open("aoc5-input.txt")
rls=lines.readlines()
last=rls[-1]
itrls=iter(rls)
high=0
highid=[0,0]
blank=0

def validate(key,value):
    if key=='byr' and int(value) <= 2002 and int(value) >= 1920:
        return True
    elif key=='iyr' and int(value) <= 2020 and int(value) >= 2010:
        return True
    elif key=='eyr' and int(value) <= 2030 and int(value) >= 2020:
        return True
    elif key=='hgt' and ("cm" in value or "in" in value):
        hgtval=int(value[:-2])
        if "cm" in value and hgtval >= 150 and hgtval <= 193:
            return True
        elif "in" in value and hgtval >= 59 and hgtval <= 76:
            return True
    elif key=='hcl' and value[:1] == "#" and len(value)==7:
        allowed=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        strippedval=value[1:]
        for x in strippedval:
            if x not in allowed:
                return False
        return True

    elif key=='ecl' and (value=='amb' or value=='blu' or value=='brn' or value=='gry' or value=='grn' or value=='hzl' or value=='oth'):
        return True
    elif key=='pid' and value.isnumeric() and len(value)==9:
        return True
    elif key=='cid':
        return True;
    else:
        return False

seats=[""]* 128

for line in itrls:
    p1=line.strip()[:-3]
    p2=line.strip()[-3:]
    lrow=0
    urow=127
    lcol=0
    ucol=7
    count=0
    for i in p1:
        if i=="F":
            urow-=int((urow-lrow)/2)
        if i=="B":
            lrow+=int((urow-lrow+1)/2)
    for j in p2:
        if j=="L":
            ucol-=int((ucol-lcol)/2)
        if j=="R":
            lcol+=int((ucol-lcol+1)/2)

    frow=min(lrow,urow)
    fcol=min(lcol,ucol)
    seats[frow] = seats[frow]+str(fcol)
    oldhigh=high
    high=max(high,(frow*8)+fcol)
    if high!=oldhigh:
        highid[0]=frow
        highid[1]=fcol

sc=0
for row in seats:
    seats[sc]=sorted(row)
    print(f"{sc}: {seats[sc]}")
    sc+=1
#print(seats)
print(f"high: {high} {highid}")
lines.close()
