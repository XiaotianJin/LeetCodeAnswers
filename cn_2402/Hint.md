> <small>开始 2025年12月27日09:13:55</small>
# 暴力法
定义一个二维数组 $booked$ ，大小是 $n*max(end_i)*n = 100*5*10^5*100$ ，全部初始化为0，最后又\*n是因为可能出现单一房间的情况
定义一个一维数组 $fist\_end\_time$ ，大小是 $n$ ，初始化为 $-1$ ，用于记录第 $i$ 个房间的最早结束时间
对某一meeting的 $start_i$ 和 $end_i$ ，执行以下逻辑：
1. 如果 $booked[j][start_i]$ 和 $booked[j][end_i-1]$ 均为0，说明当前可以直接开会，预定该房间，令 $booked[j][start_i]$ 到 $booked[j][end_i-1]$ 中的所有元素改为 $i$ ，用于标记已预订，设定 $fist\_end\_time[i]$ 为 $end_i$ ，并跳出循环，开始下一个meeting
2. 如果不满足 步骤1 之条件，则说明该房间被占用，继续向后遍历寻找可用房间
3. 如果2跑完以后，仍然未发现可用房间，那么会议延期，需要找到 $j$ 最小的最早结束会议的房间
   1. 找到 $fist\_end\_time$ 中最小的元素 $min\_time$，下标为 $idx_{min}$
   2. 找到 $booked[idx_{min}]$ 中最小的元素 $min\_itme$，按照2的逻辑预定该房间，开始下一个meeting
4. 直到遍历完所有meeting，开始求取最终结果
5. 遍历 $booked$ ，找到 $booked[i]$ 中元素种类最多的房间，即为最终结果
> XT: 
> - 这个方法可以暴力求解出结果，空间复杂度高达恐怖的 $n*n*m$，时间复杂度高达 $O(n*n*m)$，认为不可用，开始优化

# 优化1
可以注意到，对二维数组的操作直接或者间接占用了绝大部分的cpu，除了个别极端场景，暴力法中定义的二维数组 $booked$ 大概率是一个尾巴上有大量0的稀疏矩阵，那么我们可以不可以不用二维数组来处理订单呢？

注意到题目的要求：
> 会议将会按以下方式分配给会议室：
> 1. 每场会议都会在未占用且编号 **最小** 的会议室举办。
> 2. 如果没有可用的会议室，会议将会延期，直到存在空闲的会议室。延期会议的持续时间和原会议持续时间 **相同**。
> 3. 当会议室处于未占用状态时，将会优先提供给原 **开始** 时间更早的会议。

且题目对输出的需求是：
> 返回举办最多次会议的房间 **编号** 。如果存在多个房间满足此条件，则返回编号 **最小** 的房间。

其实我们不需要把实际上的订单模拟出来，假设所有会议按照 $start_i$ 升序排序进入，那么其实我们只需要维护每个房间的 $end_{room} = last\_meeting.end$ 即可快速求取出可用的房间，并按照规则分配会议即可。

注意到题目没有说输入的 $mettings$ 是有序的，所以应当先进行排序。

逻辑如下：
1. 对meetings进行排序，将所有meetings按照 $start_i$ 升序排序
2. 定义一个一维数组 $room\_end\_hour$ ，大小是 $n$ ，初始化为 $-1$ ，用于记录第 $i$ 个房间的会议结束时间
3. 定义一个一维数组 $room\_called\_count$ ，大小是 $n$ ，初始化为 $0$ ，用于记录第 $i$ 个房间被分配的会议次数
4. 遍历meetings，对于每个meeting，执行以下逻辑：
   1. 找到 $room\_end\_hour$ 中最小的元素 $min\_time$，下标为 $idx_{min}$
   2. 如果 $min\_time <= start_i$ 说明该房间直接可用，预定该房间，令 $room\_end\_hour[idx_{min}] = end_i$ ，令 $room\_called\_count[idx_{min}] += 1$ ，并跳出循环，开始下一个meeting
   3. 如果 $min\_time > start_i$ 说明该房间被占用，但是因为它是最小的，所以我们仍然分配会议到这里，令 $room\_end\_our[idx_{min}] += (end_i - start_i)$ ，令 $room\_called\_count[idx_{min}] += 1$ ，并跳出循环，开始下一个meeting
5. 直到遍历完所有meeting，开始求取最终结果
6. 遍历 $room\_called\_count$ ，找到 $room\_called\_count$ 中元素最大的房间，即为最终结果

> XT: 
> - 这个方法所需要的空间复杂度是 $2n$ 时间复杂度是 $O(m*[求最小元素（步骤4.1）的复杂度]) + O(步骤6) + O(步骤1)$
> - 这个方法的复杂度程度受到步骤4.1的影响最大
> - 步骤4.1中求取 $room\_end\_hour$ 中最小的元素时 $room\_end\_hour$ 和 $room\_called\_count$ 大概率不是有序的，且中间存在$update$的操作，所以不能用最小堆来存储，我们考虑这种场景，暴力法好像是最方便的一个方法？
>   - 有什么数据结构，可以保持有序，并且$update$操作（或者$delete+insert$）复杂度小于 $O(n)$ 吗？
>   - 有的，平衡二叉搜索树，比如红黑树，可以保持有序，并且$update$操作（或者$delete+insert$）复杂度为 $O(\log n)$
>   - 但是，让我手撕二叉树还是太复杂了，先试试线性的看能不能过题
>   - 或者直接维护最大堆呢？不管了，先试试线性，不行再改最大堆吧
> <small> 2025年12月27日09:40:16 </small>

# Failed case 1
- 题目要求 
   > 每场会议都会在未占用且编号 最小 的会议室举办。
- 步骤4.1中取最小的并不是正确的实现，而是如果取到-1，就应该找出所有的合法的房间检查一次，因为可能出现id更小但是结束时间跟靠后的那个房间

# Failed case 2
- 代码编写不仔细
```python
    if this_valid_min_hour < meeting_start_hour:
        this_room_next_end = meeting_end_hour
    else:
        # this_room_next_end = meeting_end_hour + (meeting_end_hour - meeting_start_hour)
        this_room_next_end = this_room_next_end + (meeting_end_hour - meeting_start_hour)
```

# Failed case 3
- 代码编写不仔细
```python
    # if i < min_id_in_all_possible_tuples:
    if room_id < min_id_in_all_possible_tuples:
        # min_id_in_all_possible_tuples = i
        min_id_in_all_possible_tuples = room_id
        other_valid_min_hour, other_valid_room_id = min_hour, room_id
        idx = i
```

# Failed case 4
- 代码编写不仔细
```python
    # ... min_hour < meeting_start_hour
    ... min_hour < = meeting_start_hour
```

# Failed case 5
- 代码编写不仔细
```python
    if this_valid_min_hour < meeting_start_hour:
        this_room_next_end = meeting_end_hour
    else:
        # this_room_next_end = this_room_next_end + (meeting_end_hour - meeting_start_hour)
        this_room_next_end = this_valid_min_hour + (meeting_end_hour - meeting_start_hour)
```

# Failed case 6
- Failed case 1的补丁思路不对，就算第一个不是-1也有可能有更优结果
- passed, 963ms，怎么有人100ms就搞完了阿， Solution1

# 优化
我不理解，现在算法的复杂度应该是 $常数I * n * log_2n$ 了，为啥比别人慢这么多（只有5%）？
等下，我现在是用一个最小堆来模拟，对堆的操作太多了，有没有可能减少对堆的操作呢？
试着思考一下：
1. 对meetings进行排序，将所有meetings按照 $start_i$ 升序排序
2. 维护两个最小堆，一个是busy，用结束时间排序，另一个是free，用id排序
3. 数组或者map存一下每个会议室的使用次数
4. 遍历meetings，对于每个meeting，执行以下逻辑：
   1. 检查busy堆顶的会议室和free堆顶的会议室，选取id小的那个使用，执行4.2/4.3操作
   2. 如果用的是busy堆的，不用操作，直接维护即可
   3. 如果用的是free堆的，挪动到busy堆
5. 检查会议次数最大的那个会议室，即为最终结果
不对，这样会遇到Failed case1的问题

是不是可以做一个类似滑动窗口的设定？
我知道了，这样玩
1. 对meetings进行排序，将所有meetings按照 $start_i$ 升序排序
2. 维护一个最小堆 $busy$ ，用结束时间排序，初始化为 $(-1, id)...$
3. 维护一个最小堆 $free$ , 表示当前会议所有可能可用的会议室
4. 遍历meetings，对于每个meeting，执行以下逻辑：
   1. 当 $busy$ 堆顶的结束时间小于等于当前meeting的开始时间，弹出 $busy$ 堆顶，插入到 $free$ 堆中
   2. 如果 $free$ 堆为空，说明没有可用的会议室，延期，弹出 $busy$ 堆顶，插入到 $free$ 堆中
   3. 此时 $free$ 里至少会有一个值，选取 $free$堆顶，就是可用会议室，维护会议室次数
5. 输出结果

不对，尝试写了一下这样case会出问题，并且复杂度没有降低

