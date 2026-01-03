# 暴力法

这个暴力法肯定不行，都要我对 $10^9+7$ 取余数了，肯定超时。

# 找找规律

n=1时有
``` text
RYR YRY GRY
RYG YRG GRG
RGR YGR GYR
RGY YGY GYG
```
12种情况

按照ABA和ABC两种模式（首尾相同和首尾不同），下一行的数量有

ABA模式：
``` text
ABA
BAB BCB CAC
CAB BAC
```

ABC模式：
``` text
ABC
BCA CAB
BCB BAB
```

当n=1时
ABA模式有 ABA ACA BCB BAB CAC CBC 6种情况
ABC模式有 ABC ACB BAC BCA CAB CBA 6种情况

所以可以转换成数学问题
第i行的ABA数量和ABC的数量有
$f_{aba}(1) = 6 f_{a}(1)=6$
$f_{aba}(i) = f_{aba}(i-1)*3 + f_{abc}(i-1)*2$
$f_{abc}(i) = f_{aba}(i-1)*2 + f_{abc}(i-1)*2$
所以第i行的总数就有
$f_{sum}(i) = f_{aba}(i) + f_{abc}(i)$

代入i=2验算
$f_{aba}(2) = 6*3 + 6*2 = 30$
$f_{abc}(2) = 6*2 + 6*2 = 24$
$f_{sum}(2) = 30 + 24 = 54$

似乎正确了，写一下看看