from typing import List

class Solution:
    def findMaxConsecutiveOnes(nums: List[int]) -> int:
        count = 0
        max_count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                if max_count < count:
                    max_count = count
                count = 0

        return max_count if max_count > count else count

print(Solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))