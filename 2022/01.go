package main
import (
	"fmt"
	"os"
	"strconv"
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

func p1(x []int) int{
	max:=0
	val:=0
	for i:=range x {
		if x[i]==0 {
			if val>max {
				max=val
			}
			val=0
		} else {
			val+=x[i]
		}
	}
	return max
}

func p2(x []int) int{
	top3:=0
	val:=0
	amts:=make([]int,0)
	for i:=range x {
		if x[i]==0 {
			amts=append(amts,val)
			val=0
		} else {
			val+=x[i]
		}
	}
	sort.Sort(sort.IntSlice(amts))
	top3+=amts[len(amts)-1]+amts[len(amts)-2]+amts[len(amts)-3]
	return top3
}

func main() {
	// read whole file
	text, err := os.ReadFile("01.txt")
	check(err)

	// split intput text on value; store in slice
	splitter:="\n"
	txt:=strings.Split(string(text),splitter)
	// convert to int slice
	num:=make([]int, len(txt))
	for i,s:=range txt{
		num[i], _ = strconv.Atoi(s)
	}
	//psliceS(txt)
	//bkup:=make([]int, len(num))
	//copy(bkup, num)
	//psliceI(bkup)
	z:=p1(num)
	fmt.Printf("P1 answer: %d \n",z)
	y:=p2(num)
	fmt.Printf("P2 answer: %d \n",y)
}

