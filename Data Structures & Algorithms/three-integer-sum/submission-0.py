class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            first = nums[i]
            left = i+1
            right = len(nums)-1
            if (i>0 and nums[i]==nums[i-1]):
                    continue
            else:
                while left < right:
                    total = nums[left] + nums[right]
                    if total < -first:
                        left+=1
                    elif total > -first:
                        right-=1
                    else:
                        res.append([first, nums[left], nums[right]])
                        left+=1
                        right-=1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1

        return res
               
        