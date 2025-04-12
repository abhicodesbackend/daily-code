package main

import (
	"fmt"
	"os"
	"strconv"
)

func print() {
	var s, sep string

	for i := 1; i < len(os.Args); i++ {
		s += sep + os.Args[i]
		sep = " "
	}

	fmt.Println(s)
}

func sum() {
	var sum int

	for i := 1; i < len(os.Args); i++ {
		num, err := strconv.Atoi(os.Args[i])
		if err != nil {
			fmt.Println("Conversion failed:", err)
		}
		sum += num
	}

	fmt.Println(sum)
}

func main() {
	// print()
	sum()
}