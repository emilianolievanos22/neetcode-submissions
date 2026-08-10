class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_counter = 0
    
        for i in range(0,len(nums)):
            # [1,1,0,1,1,1]
                # 1 == 1
                #counter = 1
                # 1 == 1
                # counter = 2
                # 2 == 1 NO
                # counter = 0
                # 1 == 1
                # counter = 1 
                # 1 == 1
                #counter = 2
                # 1 == 1
                #counter = 3
            if nums[i] == 1:
                counter = counter + 1
                if counter > max_counter:                    
                    max_counter = counter
                    
            else :
                counter = 0
    
        return max_counter


