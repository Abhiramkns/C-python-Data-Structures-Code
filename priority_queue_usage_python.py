# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
#
# An integer a is closer to x than an integer b if:
#
#    1) |a - x| < |b - x|, or
#    2) |a - x| == |b - x| and a < b


import heapq as hp # heapq provides data structures implementation of priority queue.
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        diff = []
        for i in arr:
            diff.append((abs(i-x), i))
    
        hp.heapify(diff)
        ans = []
        for c in range(k):
            res = hp.heappop(diff)
            ans.append(res[1])
        ans.sort()
        return ans