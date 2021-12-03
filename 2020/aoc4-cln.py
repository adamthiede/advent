#!/usr/bin/env python3
#f=open("aoc3-input.txt")
lines=open("aoc4-input-cln.txt")
#lines=f.readlines()
rls=lines.readlines()
last=rls[-1]
itrls=iter(rls)
valid=0
blank=0
lndict={} 
for line in itrls:
    if line != "" and line != "\n":
        #ln=line.split(" ")
        for x in ln:
            y=x.split(":")
            lndict[y[0]] = y[1].strip()
        if 'byr' and 'iyr' and 'eyr' and 'hgt' and 'hcl' and 'ecl 'and 'pid' in lndict:
            print(lndict)
            valid+=1
    else:
        blank+=1
        lndict.clear()
     
print(f"count: {valid}")
print(f"blank: {blank}")
lines.close()
