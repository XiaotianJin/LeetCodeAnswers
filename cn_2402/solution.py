from typing import List
import heapq

class Solution1:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 2025年12月27日16:56:10
        # 2025年12月27日18:29:53 passed，中间吃饭40min左右
        meetings.sort(key=lambda x: x[0]) # 对meetings排序，按照开始时间升序排序
        room_end_hour = [(-1, i) for i in range(n)]
        heapq.heapify(room_end_hour)
        room_booked_count = {i: 0 for i in range(n)}
        
        max_room_called_count = 0
        max_room_called_id = -1
        
        
        for meeting in meetings:
            meeting_start_hour, meeting_end_hour = meeting
            this_valid_min_hour, this_valid_room_id = heapq.heappop(room_end_hour)
            other_valid_min_hour, other_valid_room_id, idx = None, None, None
            min_id_in_all_possible_tuples = n+1
            for i, (min_hour, room_id) in enumerate(room_end_hour):
                if min_hour != -1 and room_id < this_valid_room_id and min_hour <= meeting_start_hour:
                    if room_id < min_id_in_all_possible_tuples:
                        min_id_in_all_possible_tuples = room_id
                        other_valid_min_hour, other_valid_room_id = min_hour, room_id
                        idx = i
                
                if other_valid_room_id is not None:
                    if other_valid_min_hour <= meeting_start_hour and other_valid_room_id < this_valid_room_id:
                        room_end_hour.remove(room_end_hour[idx])
                        heapq.heappush(room_end_hour, (this_valid_min_hour, this_valid_room_id)) # 恢复
                        this_valid_room_id = other_valid_room_id
                        this_valid_min_hour = other_valid_min_hour
            if this_valid_min_hour < meeting_start_hour:
                this_room_next_end = meeting_end_hour
            else:
                this_room_next_end = this_valid_min_hour + (meeting_end_hour - meeting_start_hour)
            heapq.heappush(room_end_hour, (this_room_next_end, this_valid_room_id))
            room_booked_count[this_valid_room_id] += 1
            if room_booked_count[this_valid_room_id] > max_room_called_count:
                max_room_called_count = room_booked_count[this_valid_room_id]
                max_room_called_id = this_valid_room_id
            elif room_booked_count[this_valid_room_id] == max_room_called_count and this_valid_room_id < max_room_called_id:
                max_room_called_id = this_valid_room_id
        
        return max_room_called_id

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        
        free = list(range(n))  # 初始时，所有房间都空闲
        busy = []  # (结束时间，id)， 最小堆
        counter = [0] * n
        
        for start, end in meetings:
            # 处理结束时间早于当前时间的会议
            while busy and busy[0][0] <= start:
                heapq.heappush(free, heapq.heappop(busy)[1])
            
            if free:
                i = heapq.heappop(free)
            else:
                e, i = heapq.heappop(busy)
                end += e - start
            
            heapq.heappush(busy, (end, i))
            counter[i] += 1
    
        return counter.index(max(counter))

if __name__ == '__main__':
    only_first_case = False
    input_list = [
        (4, [[48,49],[22,30],[13,31],[31,46],[37,46],[32,36],[25,36],[49,50],[24,34],[6,41]], 0), # Falied case 6
        (4, [[12,44],[27,37],[48,49],[46,49],[24,44],[32,38],[21,49],[13,30]], 1), # Falied case 5
        (3, [[1,27],[29,49],[47,49],[41,43],[15,36],[11,15]], 1), # Falied case 4
        (5, [[12,18],[8,11],[19,20],[5,11]], 0), # Falied case 3
        (2, [[10,11],[2,10],[1,17],[9,13],[18,20]], 1), # Falied case 2
        (4, [[18,19],[3,12],[17,19],[2,13],[7,10]], 0), # Failed case 1
        (2, [[0, 10], [1, 5], [2, 7], [3, 4]], 0),
        (3, [[1,20],[2,10],[3,5],[4,9],[6,8]], 1),
    ]
    failed_case = []
    for i, (n, meetings, ans) in enumerate(input_list):
        res = Solution().mostBooked(n, meetings)
        print("Res = ", res, " Ans = ", ans, " pass = ", res == ans, " case = ", i)
        if res != ans:
            failed_case.append((i, n, meetings, ans, res))
        if only_first_case:
            break
    
    if len(failed_case) == 0:
        print("!All case pass!")
    else:
        print("XXX Failed case:")
        for case in failed_case:
            print(case)