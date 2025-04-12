package main

import (
	"fmt"
	"os"
	"strconv"
)

func print() {
	var s, sep string

	for i := 2; i < len(os.Args); i++ {
		s += sep + os.Args[i]
		sep = " "
	}

	fmt.Println(s)
}

func sum() {
	var sum int

	for i := 2; i < len(os.Args); i++ {
		num, err := strconv.Atoi(os.Args[i])
		if err != nil {
			fmt.Println("Conversion failed:", err)
		}
		sum += num
	}

	fmt.Println(sum)
}

func main() {

	if len(os.Args) > 1 && os.Args[1] == "add" {
		sum()
	} else {
		print()
	}
}