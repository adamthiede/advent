package main
import (
	"fmt"
	"os"
	//"strconv"
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

func p1(s [string]){
}

func main() {
	// read whole file
	text, err := os.ReadFile("03.txt")
	check(err)

	var txt []string
	var txt1 []string
	var txt2 []string
	txt=strings.Split(string(text),"\n")
	txt1=strings.Split(string(txt[0]),",")
	txt2=strings.Split(string(txt[1]),",")
	psliceS(txt1)
	psliceS(txt2)
}

