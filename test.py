from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i, val in enumerate(nums):
            temp = target - val

            if temp in data and i != data[temp]:
                return [data[temp], i]

            data[val] = i
            print(data)







s = Solution()

print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))