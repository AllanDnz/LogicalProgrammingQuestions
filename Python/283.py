class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        i = 0
        j = 0
        
        while i < n:
            if nums[i] != 0: #if the number is not zero, then we move it to the front
                nums[j] = nums[i] #move the number to the front
                j += 1
            i += 1
        
        while j < n: #fill the rest of the array with zeros
            nums[j] = 0
            j += 1