class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        leftMax,rightMax = 0,0
        s=0
        water = 0
        while left <= right:
            if (leftMax < rightMax or leftMax == rightMax):
                leftMax = max(height[left],leftMax)
                water = leftMax - height[left]
                left+=1
                
            else:
                rightMax = max(height[right], rightMax)
                water = rightMax - height[right]
                right -=1
            s+=water
        return s
            

        