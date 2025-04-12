package main

import (
	"fmt"
	"os"
	"strings"
)

func printArgs1() {
	// s := ""
	// var s = ""
	// var s string
	// var s string = ""

	fmt.Println(strings.Join(os.Args[1:], " "))
}

func printArgs2() {

	for i,v := range os.Args[1:] { // _ can be used in place of i if index is not of use in current scope
		fmt.Println("index: ", i, "value: ", v)
	}
}

func main() {
	printArgs1()
	printArgs2()
}