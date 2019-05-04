


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxResult = nums[0]
        tempRes = 0
        for x in nums:
            tempRes += x
            if tempRes > maxResult:
                maxResult = tempRes
            if tempRes < 0:
                tempRes = 0
                continue
        return maxResult

if __name__ == "__main__":
    inputArray = [-2,1,-3,4,-1,2,1,-5,4]
    res = Solution().maxSubArray(inputArray)
    print res