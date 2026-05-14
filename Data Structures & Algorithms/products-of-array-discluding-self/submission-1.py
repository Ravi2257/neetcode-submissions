import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        parr = []
        for i in range(len(nums)):
            new_list = [val for index, val in enumerate(nums) if index != i]
            parr.append(math.prod(new_list))
        return parr