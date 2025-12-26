package main

import "fmt"

func bestClosingTime(customers string) int {
	mp := 0
	p := 0
	ans := 0
	for i := 0; i < len(customers); i++ {
		if customers[i] == 'N' {
			p++
		} else {
			p--
		}
		if p < mp {
			mp = p
			ans = i + 1
		}
	}
	return ans
}

type InputData struct {
	customers     string
	answer        int
	output_answer int
}

func main() {
	input_list := []InputData{
		{"YYNY", 2, -1},
		{"NNNNN", 0, -1},
		{"YYYYY", 5, -1},
		{"YN", 1, -1},
		{"YNYNNNYYY", 1, -1},
	}
	not_passed_data := []InputData{}
	for input := range input_list {
		input_list[input].output_answer = bestClosingTime(input_list[input].customers)
		if input_list[input].output_answer != input_list[input].answer {
			fmt.Printf(" XXXX Input: %s, Expected: %d, Output: %d, Passed: %t\n", input_list[input].customers, input_list[input].answer, input_list[input].output_answer, (input_list[input].output_answer == input_list[input].answer))
			not_passed_data = append(not_passed_data, input_list[input])
		}
	}
	if len(not_passed_data) == 0 {
		fmt.Println("! All test cases passed !")
	}
}
