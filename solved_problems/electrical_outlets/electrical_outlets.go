package main

import (
	"fmt"
)

func main() {
	var numTestCases int

	fmt.Scanln(&numTestCases)

	for i := 0; i < numTestCases; i++ {
		var numPowerStrips int
		fmt.Scan(&numPowerStrips)
		var plugs int
		for p := 0; p < numPowerStrips; p++ {
			var powerStrip int
			fmt.Scan(&powerStrip)
			if p == numPowerStrips-1 {
				plugs += powerStrip
			} else {
				plugs += powerStrip - 1
			}
		}

		fmt.Println(plugs)
	}
}
