package main

import (
	"fmt"
)

func successRate(total int, failed int) float64 {
	if total == 0 {
		return 0
	}

	// Bug: integer division truncates before conversion.
	success := (total - failed) / total
	return float64(success) * 100
}

func main() {
	total := 9
	failed := 2
	fmt.Println(successRate(total, failed))
}
