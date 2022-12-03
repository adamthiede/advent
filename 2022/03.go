package main
import (
	"fmt"
	"os"
//	"strconv"
	"strings"
	"sort"
)

// slice printer from go tour
func psliceS(s []string) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}
func psliceI(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}
// error checker helper function
func check(e error) {
	if e != nil {
		panic(e)
	}
}
func p3(l string) int{
	var vals=map[string]int{"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26, "A":27, "B":28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36, "K":37, "L":38, "M":39, "N":40, "O":41, "P":42, "Q":43, "R":44, "S":45, "T":46, "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52, }
	return vals[l]
}

func p1(x []string) int{
	score:=0
	for i,a:=range x {
		mid:=len(a)/2
		b:=strings.Split(a[:mid],"")
		c:=strings.Split(a[mid:],"")
		sort.Strings(b)
		sort.Strings(c)
		// find common thing
		common:=""
		for w:=range b {
			for z:=range c {
				if b[w]==c[z] {
					common=b[w]
					break
				}
			}
			if common!="" {
				break
			}
		}
		commonscore:=p3(common)
		score+=commonscore
		fmt.Printf("%d:%d %s %s, %s\n",i,commonscore,b,c,common)
	}
	return score
}

func p2(x []string) int{
	score:=0
	i:=0
	for i<=len(x)-1 {
		//e1:=strings.Split(x[i],"")
		//e2:=strings.Split(x[i+1],"")
		//e3:=strings.Split(x[i+2],"")
		e1:=x[i]
		e2:=x[i+1]
		e3:=x[i+2]
		common:=""
		for _,a:=range e1 {
			if strings.Contains(e2,string(a)) && strings.Contains(e3,string(a)) {
				common=string(a)
				break
			}
		}
		score+=p3(common)
		fmt.Printf("%s: %d %s, %d %s, %d %s\n\n",common,i,e1,i+1,e2,i+2,e3)
		i+=3
	}
	return score
}

func main() {
	// read whole file
	text, err := os.ReadFile("03.txt")
	check(err)

	// split intput text on value; store in slice
	splitter:="\n"
	txt:=strings.Split(string(text),splitter)
	txt=txt[:len(txt)-1]
	// convert to int slice
	//num:=make([]int, len(txt))
	//for i,s:=range txt{
	//	num[i], _ = strconv.Atoi(s)
	//}
	//psliceS(txt)
	//bkup:=make([]int, len(num))
	//copy(bkup, num)
	//psliceI(bkup)
	//z:=p1(txt)
	//fmt.Printf("P1 answer: %d \n",z)
	y:=p2(txt)
	fmt.Printf("P2 answer: %d \n",y)
}

