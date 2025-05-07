class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        tsum,left=0,0
        minlen=float("inf")
        for right in range(len(nums)):
            num=nums[right]
            tsum+=num
            while tsum>=target:
                minlen=min(minlen,right-left+1)
                tsum-=nums[left]
                left+=1

        return 0 if minlen==float("inf") else minlen
        