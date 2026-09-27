class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currCount = 0
        maxCount = 0
        for n in nums:
            if n != 1:
                currCount = 0
            else:
                currCount+=1
            maxCount = max(currCount,maxCount)
        return maxCount