class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[-1]*len(nums)
        stack=[]

        for i in range(2*len(nums)):
            current=i%len(nums)
            while stack and nums[current]> nums[stack[-1]]:
                top=stack.pop()
                ans[top]=nums[current]
            if i<len(nums):
                stack.append(current)
        return ans
            

        