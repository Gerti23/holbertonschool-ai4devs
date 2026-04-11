package main

import "fmt"

func successRate(total int, failed int) float64 {
	if total == 0 {
		return 0
	}

	success := float64(total-failed) / float64(total)
	return success * 100
}

func main() {
	total := 9
	failed := 2
	fmt.Println(successRate(total, failed))
}
