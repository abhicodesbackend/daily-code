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
	defer response.Body.Close()

	fmt.Fprintf(os.Stdout, "Status in response: %s \n", response.Status)

	data,err := io.ReadAll(response.Body)
	response.Body.Close()
	if err != nil {
		fmt.Fprintf(os.Stdout, "Error in parsing data %d \n", err)
	}

	os.WriteFile("response.txt", data, 0644)
}

func main() {
	fetch()
}