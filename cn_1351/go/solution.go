package main

import "fmt"

func countNegatives(grid [][]int) int {
	if len(grid) == 0 {
		return 0
	}
	m, n := len(grid), len(grid[0])
	pos_sum := 0
	last_pos := n - 1
	for i := 0; i < m; i++ {
		for j := last_pos; j >= 0; j-- {
			if grid[i][j] >= 0 {
				pos_sum += j + 1
				last_pos = j
				break
			}
		}
	}
	return n*m - pos_sum
}

func main() {
	onlyFirstCase := -1
	inputList := []struct {
		grid [][]int
		ans  int
	}{
		{[][]int{
			{4, 3, 2, -1},
			{3, 2, 1, -1},
			{1, 1, -1, -2},
			{-1, -1, -2, -3},
		}, 8},
	}

	type failed struct {
		i, ans, res int
		grid        [][]int
	}
	var failedCase []failed

	if onlyFirstCase < 0 {
		for i, tc := range inputList {
			res := countNegatives(tc.grid)
			fmt.Printf("Res = %d Ans = %d pass = %t case = %d\n", res, tc.ans, res == tc.ans, i)
			if res != tc.ans {
				failedCase = append(failedCase, failed{i, tc.ans, res, tc.grid})
			}
		}
	} else {
		tc := inputList[onlyFirstCase]
		res := countNegatives(tc.grid)
		fmt.Printf("Res = %d Ans = %d pass = %t case = %d\n", res, tc.ans, res == tc.ans, onlyFirstCase)
		if res != tc.ans {
			failedCase = append(failedCase, failed{onlyFirstCase, tc.ans, res, tc.grid})
		}
	}

	if len(failedCase) == 0 {
		fmt.Println("!All case pass!")
	} else {
		fmt.Println("XXX Failed case:")
		for _, c := range failedCase {
			fmt.Println(c.i, c.ans, c.res)
		}
	}
}
