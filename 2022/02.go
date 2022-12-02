package main
import (
	"fmt"
	"os"
//	"strconv"
	"strings"
//	"sort"
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
	for i:=range x {
		myscore:=0
		v:=strings.TrimSpace(x[i])
		z:=strings.Split(v," ")
		switch z[1] {
		case "X":
			myscore+=1
			switch z[0] {
			case "A":
				myscore+=3
			case "C":
				myscore+=6
			}
		case "Y":
			myscore+=2
			switch z[0] {
			case "A":
				myscore+=6
			case "B":
				myscore+=3
			}
		case "Z":
			myscore+=3
			switch z[0] {
			case "B":
				myscore+=6
			case "C":
				myscore+=3
			}
		}
		fmt.Printf("Opp: %s Me: %s Scored: %d\n",z[0],z[1],myscore)
		score+=myscore
	}
	return score
}

func p2(x []string) int{
	score:=0
	for i:=range x {
		myscore:=0
		v:=strings.TrimSpace(x[i])
		z:=strings.Split(v," ")
		switch z[0] {
			// a rock b paper c scissors
			// x lose y draw z win
			// 1 rock 2 paper 3 scissors
			// 0 lose 3 draw 6 win
		case "A":
			switch z[1] {
			case "X":
				myscore+=3
			case "Y":
				myscore+=4
			case "Z":
				myscore+=8
			}
		case "B":
			switch z[1] {
			case "X":
				myscore+=1
			case "Y":
				myscore+=5
			case "Z":
				myscore+=9
			}
		case "C":
			switch z[1] {
			case "X":
				myscore+=2
			case "Y":
				myscore+=6
			case "Z":
				myscore+=7
			}
		}
		fmt.Printf("Opp: %s Me: %s Scored: %d\n",z[0],z[1],myscore)
		score+=myscore
	}
	return score
}

func main() {
	// read whole file
	text, err := os.ReadFile("02.txt")
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
	z:=p1(txt)
	fmt.Printf("P1 answer: %d \n",z)
	y:=p2(txt)
	fmt.Printf("P2 answer: %d \n",y)
}

