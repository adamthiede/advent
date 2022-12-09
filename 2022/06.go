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

func unique(intSlice []string) []string{
    keys := make(map[string]bool)
    list := []string{}
    for _, entry := range intSlice {
        if _, value := keys[entry]; !value {
            keys[entry] = true
            list = append(list, entry)
        }
    }
    return list
}

func p1(x string) int{
	arr:=strings.Split(x,"")
	for i:=0;i<=len(arr)-14;i++ {
		a1:=arr[i:i+14]
		a2:=unique(a1)
		if len(a2)==len(a1) {
			fmt.Printf("found at %d, end %d\n",i,i+14)
			psliceS(a2)
			break
		}
	}
	return 0
}

func p2(x []string) int{
	score:=0
	return score
}
func main() {
	// read whole file
	text, err := os.ReadFile("06.txt")
	check(err)
	instructions, err2 := os.ReadFile("06a.txt")
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
	//psliceS(txt)
	psliceS(ins)
	//bkup:=make([]int, len(num))
	//copy(bkup, num)
	//psliceI(bkup)
	//z:=p1(ins[0])
	z:=p1(txt[0])
	fmt.Printf("P1 answer: %d \n",z)
}
