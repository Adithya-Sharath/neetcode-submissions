class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            if (num-1 in s):
                continue
            else:
                temp = 1
                for i in range(len(nums)):
                    if (num+1 in s):
                        temp+=1
                        num+=1
                        
                    else:
                        break
            if temp > longest  :
                longest  = temp
        return longest 
            
