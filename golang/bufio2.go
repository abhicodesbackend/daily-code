package main

import (
	"fmt"
	"os"
	"bufio"
)

func findDuplicates() {
	counts := make(map[string]int)
	files := os.Args[1:]

	if len(files) == 0 {
		countLines(os.Stdin, counts)
	} else {
		for _,file := range files {
			f, err := os.Open(file)
			if err != nil {
				fmt.Println("Error in opening file: ", file)
				continue
			}
			countLines(f, counts)
			f.Close()
		}
	}

	for text,line := range counts {
		if line > 1 {
			fmt.Printf("%d: %s\n", line, text)
		}
	}
}

func countLines(f *os.File, counts map[string]int) {
	inputs := bufio.NewScanner(f)
	for inputs.Scan() {
		counts[inputs.Text()]++
	}
}

func main() {
	findDuplicates()
}