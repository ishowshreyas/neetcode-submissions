class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        
        while left <= right: 
            mid = (left + right) // 2 
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: 
                left = mid + 1     # Fixed: changed 'low' to 'left'
            else: 
                right = mid - 1    # Fixed: changed 'high' to 'right'
                
        # If the target is not found, 'left' will point to the correct insertion index
        return left
