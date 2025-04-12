package main

import (
	"fmt"
	"os"
	"strconv"
)

func forLoop() {
	sum := 0

	for i := 1; i < len(os.Args); i++ {
		num, err := strconv.Atoi(os.Args[i])
		if err != nil {
			fmt.Println("Conversion failed:", err)
		}
		sum += num
	}

	fmt.Println("Sum from for loop : ", sum)
}

func whileLoop() {
	sum := 0; i := 1

	for i < len(os.Args) {
		num, err := strconv.Atoi(os.Args[i])
		if err != nil {
			fmt.Println("Conversion failed:", err)
		}
		sum += num
		i++;
	}

	fmt.Println("Sum from while loop : ", sum);
}

func infiniteLoop() {
	sum := 0; i := 1

	for {
		if i >= len(os.Args) {
			break
		}

		num, err := strconv.Atoi(os.Args[i])
		if err != nil {
			fmt.Println("Conversion failed:", err)
		}
		sum += num
		i++;
	}

	fmt.Println("Sum from infinite loop : ", sum);
}

func main() {
	forLoop()
	whileLoop()
	infiniteLoop()
}