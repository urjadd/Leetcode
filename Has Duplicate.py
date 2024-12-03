from typing import List

class Solution:
    def hasDuplicate(self, nums : List[int]) -> bool:
        if len(nums)  == 1: return False
        nums.sort()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                return True
        return False
    
solution = Solution()
nums =  [2,3,3.3,1,3.3]
res = solution.hasDuplicate(nums)
print(res)