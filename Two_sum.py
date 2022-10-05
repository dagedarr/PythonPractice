nums = [3, 2, 4]
target = 6

res = []

for index, num in enumerate(nums):
    if (target - num in nums
            and (num * 2 != target or nums.count(num) > 1)):
        res.append(index)

print(res)
