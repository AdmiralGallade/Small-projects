#https://leetcode.com/problems/maximum-product-of-three-numbers/
from itertools import combinations
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        nums[3:len(nums)-3]=[]
        
        
         # return max(nums[i] * nums[j] * nums[k]
         # for i in xrange(len(nums))
         # for j in xrange(i+1, len(nums))
         # for k in xrange(j+1, len(nums)))
        return max(x * y * z for x,y,z in itertools.combinations(nums, 3))