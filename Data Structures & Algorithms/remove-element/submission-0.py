class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        while val in nums : 
            nums.remove(val)
        for i in range(len(nums)):
            c+=1 
        return c 
        