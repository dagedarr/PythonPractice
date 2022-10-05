def pivotIndex(nums) -> int:
        RSum = sum(nums)
        LSum = 0

        for index, num in enumerate(nums):
            RSum -= num
            if LSum == RSum:
                return index
            LSum += num
        return -1

nums = [1,7,3,6,5,6]
 
print(pivotIndex(nums))