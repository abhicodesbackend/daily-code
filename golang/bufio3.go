package main

import (
	"fmt"
	"os"
	"strings"
)

func findDuplicates() {

	counts := make(map[string]int)
	files := os.Args[1:]

	if len(files) == 0 {
		fmt.Println("No file provided to find duplicates")
		return
	}

	for _, filename := range files {
		data, err := os.ReadFile(filename)
		if err != nil {
			fmt.Println("Error in opening file: ", filename)
			continue
		}
		for _, line := range strings.Split(string(data), "\n") {
			counts[line]++
		}
	}

	for text,count := range counts {
		if count > 1 {
			fmt.Printf("%d: %s\n", count, text)
		}
	}
}

func main() {
	findDuplicates()
}