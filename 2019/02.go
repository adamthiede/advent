package main
import (
	"fmt"
	"os"
	"strconv"
	"strings"
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

func isOp(x int) bool{
	if x==1 || x==2 || x==99 {
		return true
	} else {
		return false
	}
}

func p1(x []int) int{
	x[1]=12
	x[2]=2
	for i:=0;i<len(x);{
	//for i,j:=range x{
		j:=x[i]
		a:=x[i+1]
		b:=x[i+2]
		c:=x[i+3]
		fmt.Println(i,":",j,a,b,c)
		switch j {
		case 1:
			//add
			x[c]=x[a]+x[b]
			i+=4
		case 2:
			//multiply
			x[c]=x[a]*x[b]
			i+=4
		case 99:
			fmt.Print("99,end\n")
			psliceI(x)
			return x[0]
		default:
			fmt.Println(i,j,"not an opcode")
			break
		}
	}
	return 0
}
func p2(x []int, y int, z int) int{
	x[1]=y
	x[2]=z
	for i:=0;i<len(x);{
	//for i,j:=range x{
		j:=x[i]
		a:=x[i+1]
		b:=x[i+2]
		c:=x[i+3]
		//fmt.Println(i,":",j,a,b,c)
		switch j {
		case 1:
			//add
			x[c]=x[a]+x[b]
			i+=4
		case 2:
			//multiply
			x[c]=x[a]*x[b]
			i+=4
		case 99:
			fmt.Print("99,end\n")
			psliceI(x)
			return x[0]
		default:
			fmt.Println(i,j,"not an opcode")
			os.Exit(1)
		}
	}
	return 0
}

func main() {
	// read whole file
	text, err := os.ReadFile("02.txt")
	check(err)

	// split intput text on value; store in slice
	splitter:=","
	txt:=strings.Split(string(text),splitter)
	// convert to int slice
	num:=make([]int, len(txt))
	for i,s:=range txt{
		num[i], _ = strconv.Atoi(s)
	}
	//psliceS(txt)
	//psliceI(num)
	//fmt.Println(p1(num))
	bkup:=make([]int, len(num))
	copy(bkup, num)
	psliceI(bkup)

	for i:=0;i<100;i++{
		for j:=0;j<100;j++{
			fmt.Println(i,j)
			copy(num,bkup)
			if p2(num,i,j)==19690720 {
				ans:=100*i+j
				fmt.Println(i,j,ans)
				os.Exit(0)
			}
		}
	}
}

