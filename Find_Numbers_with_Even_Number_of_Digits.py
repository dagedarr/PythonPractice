from typing import List


class Solution:
    def findNumbers(nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count



print(Solution.findNumbers([12,345,2,6,7896]))
        