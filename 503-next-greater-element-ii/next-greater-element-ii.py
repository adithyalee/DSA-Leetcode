class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        ans=[-1]*len(nums)
        stack=[]

        for i in range(2*len(nums)):
            curr=i%len(nums)
            while stack and nums[curr]> nums[stack[-1]]:
                index=stack.pop()
                ans[index]= nums[curr]
            if i<len(nums):
                stack.append(i)
        return ans
        