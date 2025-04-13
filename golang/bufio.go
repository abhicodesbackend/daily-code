package main

import (
	"bufio"
	"os"
	"fmt"
)

func findDuplicates() {
	counts := make(map[string]int)
	inputs := bufio.NewScanner(os.Stdin)

	for inputs.Scan() {
		counts[inputs.Text()]++
	}

	for text, count := range counts {
		if count > 1 {
			fmt.Printf("%d: %s\n", count, text)
		}
	}
}

func main() {
	findDuplicates()
}