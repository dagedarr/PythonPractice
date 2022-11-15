from typing import List


class Solution:
    def sortedSquares(nums: List[int]) -> List[int]:
        return sorted([i**2 for i in nums])


print(Solution.sortedSquares([-7,-3,2,3,11]))
        