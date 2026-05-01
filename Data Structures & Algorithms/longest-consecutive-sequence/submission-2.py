class Solution:
        def longestConsecutive(self, nums: List[int]) -> int:
            
            sor = set(nums)
            longest = 0

            for num in sor:
                if (num-1) not in sor:
                    len = 1
                    while (num+len) in sor:
                        len += 1
                    longest = max(len, longest) 
            return longest