- 本质上是一个求有几个1的问题
- 在关门的那个小时以后进行反向计数，看有几个0，加上前面的1，就是结果
- 暴力法
  - 单次检查必定遍历完全字符串，时间复杂度为O(n)
  - 要遍历所有的时间成本，所以外层还要一个O(n)的循环
  - 所以总时间复杂度为O(n^2)
- 优化
  - 用空间换时间
    - 存储两个长度为n的数组Postive和Negative
    - 其中 Postive[i]表示0~i位中1的个数
    - 其中 Negative[i]表示i+1~n位中0的个数
    - 每次检查只要直接获取 Postive[i] + Negative[i] 即可

简表如下：
```text
       Y Y N Y
       0 0 1 0
idx  0 1 2 3 4
pos  0 0 0 1 1
neg  3 2 1 1 0
RES  3 2 1 2 1
```

    - Passed，179ms，Solution1

  - 更进一步
    - 我在计算Negative的时候就可以直接把RES结果算出来，并且维护出正确的ANS了，可以少遍历一次
    - Passed, 189ms，Solution2，好像没啥明显提升

  - 更进一步
    - 那么Negetive的遍历可以去掉吗？把复杂度压到O(N)
    - 我有一个10长的1和0组成的序列
    - 当我直到每一位的前面有几个1的时候，我有办法知道后面有几个0吗？

``` text
       Y N Y N N N Y Y Y
idx  0 1 2 3 4 5 6 7 8 9
       0 1 0 1 1 1 0 0 0
pos  0 0 1 1 2 3 4 4 4 4
neg  5 4 4 3 3 3 3 2 1 0
res  5 4 5 4 5 6 7 6 5 4
```

- 想不到怎么解，看看别人的答案
```python
        min_penalty = penalty = ans = 0
        for i,c in enumerate(customers):
            if c == "N":
                penalty += 1
            else:
                penalty -= 1

            if penalty < min_penalty:
                min_penalty = penalty
                ans = i+1
```

-  为什么可以呢？
    - 第j个小时的代价 = 0~j小时内有几个N(N<sub>0j</sub>) + j小时后面几个Y(Y<sub>jn</sub>)
    - j小时后面几个Y(Y<sub>jn</sub>) = 总Y数量(CountY) - 0~j小时内有几个Y(Y<sub>0j</sub>)
    - 所以第j个小时的代价 = 0~j小时内有几个N(N<sub>0j</sub>) + j小时后面几个Y(Y<sub>jn</sub>) = N<sub>0j</sub> + Y<sub>jn</sub> = N<sub>0j</sub> + CountY - Y<sub>0j</sub>
    - 因为CountY是常量，且题目不关注具体的代价值，所以第j个小时的代价可以简化为 = N<sub>0j</sub> - Y<sub>0j</sub>
    - 证明完成
