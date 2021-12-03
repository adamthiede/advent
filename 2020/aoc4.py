#!/usr/bin/env python3
#f=open("aoc3-input.txt")
lines=open("aoc4-input.txt")
#lines=f.readlines()
rls=lines.readlines()
last=rls[-1]
itrls=iter(rls)
valid=0
blank=0
lndict={} 

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

for line in itrls:
    if line != "\n":
        #print(f"LINE {line.strip()} EOL")
        x=line.split(" ")
        for y in x:
            z=y.split(":")
            if (validate(z[0],z[1].strip())):
                lndict[z[0]] = z[1].strip()
                #print(f"adding {z[0]}={z[1].strip()} to lndict")

    elif line=="\n":
        blank+=1
        lndict.clear()
     
    if 'byr' in lndict  and 'iyr' in lndict and 'eyr' in lndict and 'hgt' in lndict and 'hcl' in lndict and 'ecl'in lndict and 'pid' in lndict:
        print(lndict)
        valid+=1
        lndict.clear()
    
print(f"count: {valid}")
print(f"blank: {blank}")
lines.close()
