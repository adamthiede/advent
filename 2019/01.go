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

func p1(s []int) int {
	tot:=0
	for i:=0;i<len(s);i++ {
		tot+=(int(s[i])/3)-2
	}
	return tot
}

func p2(s []int) int {
	tot:=0
	for i:=0;i<len(s);i++ {
		partFuel:=(int(s[i])/3)-2
		var fuelFuel=int (partFuel/3)-2
		fmt.Print("weight:",s[i]," pF:",partFuel, " fF: ", fuelFuel, "+")
		for ((fuelFuel/3)-2)>0 {
			partFuel+=fuelFuel
			fuelFuel=(fuelFuel/3)-2
			fmt.Print(fuelFuel, "+")
		}
		partFuel+=fuelFuel
		tot+=partFuel
		fmt.Print("=",partFuel,"\n")
	}
	return tot
}

func main() {
	// read whole file
	text, err := os.ReadFile("01.txt")
	check(err)
	//fmt.Printf("%s\ntext is type %T\n",string(text[3]),text)

	// parse whole file
	var txt []string
	var num []int
	word:=""
	for i:=0;i<len(text);i++ {
		if string(text[i])=="\n" {
			txt=append(txt,word)
			x,e:=strconv.Atoi(strings.TrimSuffix(word,"\n"))
			check(e)
			//fmt.Printf("%d\n",x)
			num=append(num,x)
			//fmt.Printf("%s\n", word)
			word=""
		} else {
			word+=(string(text[i]))
		}
	}

	//psliceS(txt)
	//psliceI(num)
	//fmt.Println(p1(num))
	fmt.Println(p2(num))
}

