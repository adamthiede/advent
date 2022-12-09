package main
import (
	"fmt"
	"os"
//	"strconv"
	"strings"
	//"sort"
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

func p1(x []string) int{
	score:=0

	return score
}

func p2(x []string) int{
	score:=0
	return score
}
func main() {
	// read whole file
	text, err := os.ReadFile("05.txt")
	check(err)
	instructions, err2 := os.ReadFile("05a.txt")
	check(err2)

	// split intput text on value; store in slice
	splitter:="\n"
	txt:=strings.Split(string(text),splitter)
	ins:=strings.Split(string(instructions),splitter)
	txt=txt[:len(txt)-1]
	// convert to int slice
	//num:=make([]int, len(txt))
	//for i,s:=range txt{
	//	num[i], _ = strconv.Atoi(s)
	//}
	psliceS(txt)
	psliceS(ins)
	//bkup:=make([]int, len(num))
	//copy(bkup, num)
	//psliceI(bkup)
	//z:=p1(txt)
	//fmt.Printf("P1 answer: %d \n",z)
	y:=p2(txt)
	fmt.Printf("P2 answer: %d \n",y)
}
