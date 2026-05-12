class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        parr = []
        for i in range(len(nums)):
            prod = 1
            new_list = [val for index, val in enumerate(nums) if index != i]
            for j in range(len(new_list)):
                prod *= new_list[j]
            parr.append(prod)
        return parr