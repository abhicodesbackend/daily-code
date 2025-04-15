package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func fetch() {
	url := "https://catfact.ninja/fact"
	response, err := http.Get(url)
	if err != nil {
		fmt.Fprintf(os.Stdout, "Error in fetching from %d \n %d \n", url, err)
	}
	data,err := io.ReadAll(response.Body)
	response.Body.Close()
	if err != nil {
		fmt.Fprintf(os.Stdout, "Error in parsing data %d \n", err)
	}
	// fmt.Println("Response: ", string(data))
	fmt.Fprintf(os.Stdout, "Response: %s\n", data)
}

func main() {
	fetch()
}

// go run fetch.go | tee response.txt -> this will write to file and also print on terminal