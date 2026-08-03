from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        status = False
        nums_dict = Counter(nums)
        for key , val in nums_dict.items():
            if nums_dict[key] > 1 : 
                status = True
                break 
        return status
        