// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         for i in range(len(nums)):
                first = nums[i]
                value = target - nums[i]
                if value in nums:
                    j = nums.index(value)
                    if j != i:
                        answer =  str(i) + str(j)
                        return answer
