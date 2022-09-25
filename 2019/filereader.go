package main
import (
	"fmt"
	"os"
)

// slice printer from go tour
func printSlice(s []string) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}
// error checker helper function
func check(e error) {
	if e != nil {
		panic(e)
	}
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

	//fmt.Println(p1(txt))
	psliceS(txt)
	psliceI(num)
}

