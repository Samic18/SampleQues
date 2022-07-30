'''    "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
     You may assume that each input would have exactly one solution, and you may not use the same element twice."
'''

class Solution(object):
	def twoSum(self, nums, target):
		mapping = {}

		for index, val in enumerate(nums):
			difference = target - val
			if difference in mapping:
				return [mapping[difference], index]
			else:
				mapping[val] = index

s = Solution()
print(s.twoSum([[2,7,11,15]], 9))

#Output
[0,1]

# Space: O(N)
# Time: O(N)
Solution 2
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return[i,j]

print(twoSum([[2,7,11,15]], 9))

#Output
[0,1]

