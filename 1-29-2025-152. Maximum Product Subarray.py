class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def reduce(l):
            if len(l) == 0:
                return 0
            p = 1
            for n in l:
                p *= n
            return p
        if not nums:
            return 0      
        if len(nums) == 1:
            return nums[0]  
        max_p = nums[0]
        prev = 1
        fnni = -1
        for i in range(0, len(nums)):
            curr = nums[i] * prev
            max_p = max(max_p, curr)
            if curr < 0 and fnni == -1:
                fnni = i
            elif curr == 0:
                if prev < 0 and abs(prev) > max_p:
                    max_p = max(max_p, reduce(nums[fnni + 1:i]))
                prev = 1
                fnni = -1
                continue              
            prev = curr
        if curr < 0 and abs(curr) > max_p and fnni != -1 and fnni != len(nums) - 1:
            max_p = max(max_p, reduce(nums[fnni + 1:]))
        return max_p
        
