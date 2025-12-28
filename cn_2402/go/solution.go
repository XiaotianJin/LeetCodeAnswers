package main

import (
	"container/heap"
	"fmt"
	"slices"
	"sort"
)

func mostBooked(n int, meetings [][]int) (ans int) {
	slices.SortFunc(meetings, func(a, b []int) int { return a[0] - b[0] })

	idle := hp{make([]int, n)} // 会议室编号
	for i := range n {
		idle.IntSlice[i] = i
	}
	using := hp2{}        // (结束时间，会议室编号)
	cnt := make([]int, n) // 会议室的开会次数

	for _, m := range meetings {
		start, end := m[0], m[1]

		// 在 start 时刻空出来的会议室
		for len(using) > 0 && using[0].end <= start {
			heap.Push(&idle, heap.Pop(&using).(pair).i)
		}

		var i int
		if idle.Len() > 0 { // 有空闲的会议室
			i = heap.Pop(&idle).(int)
		} else {
			// 弹出一个最早结束的会议室（若有多个同时结束，弹出编号最小的会议室）
			p := heap.Pop(&using).(pair)
			end += p.end - start // 更新当前会议的结束时间
			i = p.i
		}

		heap.Push(&using, pair{end, i}) // 使用一个会议室
		cnt[i]++
	}

	for i, c := range cnt {
		if c > cnt[ans] {
			ans = i
		}
	}
	return
}

type hp struct{ sort.IntSlice }

func (h *hp) Push(v any) { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp) Pop() any   { a := h.IntSlice; v := a[len(a)-1]; h.IntSlice = a[:len(a)-1]; return v }

type pair struct{ end, i int }
type hp2 []pair

func (h hp2) Len() int { return len(h) }
func (h hp2) Less(i, j int) bool {
	a, b := h[i], h[j]
	return a.end < b.end || a.end == b.end && a.i < b.i
}
func (h hp2) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *hp2) Push(v any)   { *h = append(*h, v.(pair)) }
func (h *hp2) Pop() any     { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }

func main() {
	onlyFirstCase := -1
	inputList := []struct {
		n        int
		meetings [][]int
		ans      int
	}{
		{4, [][]int{{48, 49}, {22, 30}, {13, 31}, {31, 46}, {37, 46}, {32, 36}, {25, 36}, {49, 50}, {24, 34}, {6, 41}}, 0}, // Failed case 6
		{4, [][]int{{12, 44}, {27, 37}, {48, 49}, {46, 49}, {24, 44}, {32, 38}, {21, 49}, {13, 30}}, 1},                    // Failed case 5
		{3, [][]int{{1, 27}, {29, 49}, {47, 49}, {41, 43}, {15, 36}, {11, 15}}, 1},                                         // Failed case 4
		{5, [][]int{{12, 18}, {8, 11}, {19, 20}, {5, 11}}, 0},                                                              // Failed case 3
		{2, [][]int{{10, 11}, {2, 10}, {1, 17}, {9, 13}, {18, 20}}, 1},                                                     // Failed case 2
		{4, [][]int{{18, 19}, {3, 12}, {17, 19}, {2, 13}, {7, 10}}, 0},                                                     // Failed case 1
		{2, [][]int{{0, 10}, {1, 5}, {2, 7}, {3, 4}}, 0},
		{3, [][]int{{1, 20}, {2, 10}, {3, 5}, {4, 9}, {6, 8}}, 1},
	}

	var failedCase []struct {
		i, n, ans, res int
		meetings       [][]int
	}

	if onlyFirstCase == -1 {
		for i, tc := range inputList {
			res := mostBooked(tc.n, tc.meetings)
			fmt.Printf("Res = %d Ans = %d pass = %t case = %d\n", res, tc.ans, res == tc.ans, i)
			if res != tc.ans {
				failedCase = append(failedCase, struct {
					i, n, ans, res int
					meetings       [][]int
				}{i, tc.n, tc.ans, res, tc.meetings})
			}
		}
	} else {
		i := onlyFirstCase
		tc := inputList[i]
		res := mostBooked(tc.n, tc.meetings)
		fmt.Printf("Res = %d Ans = %d pass = %t case = %d\n", res, tc.ans, res == tc.ans, i)
		if res != tc.ans {
			failedCase = append(failedCase, struct {
				i, n, ans, res int
				meetings       [][]int
			}{i, tc.n, tc.ans, res, tc.meetings})
		}
	}

	if len(failedCase) == 0 {
		fmt.Println("!All case pass!")
	} else {
		fmt.Println("XXX Failed case:")
		for _, c := range failedCase {
			fmt.Println(c.i, c.n, c.ans, c.res)
		}
	}
}
