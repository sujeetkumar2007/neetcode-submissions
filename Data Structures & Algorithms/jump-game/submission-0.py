class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            maxJump = nums[i]
            if i + maxJump >= target:
                target = i
        return True if target==0 else False
