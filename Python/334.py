class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        first = float('inf')
        second = float('inf')
        
        for i in nums:
            if i <= first: #if the number is less than the first, then update the first
                first = i  
            elif i <= second: #if the number is less than the second, then update the second
                second = i  
            else:
                return True  
        
        return False