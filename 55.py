class Solution(object):
    # if exist a location 's' which value larger than the distance between 's' to 'e'
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target_loc = len(nums)-1
        for i in range(target_loc-1, -1, -1):
            if nums[i] >= target_loc-i:
                target_loc = i
        print target_loc
        return target_loc == 0


if __name__ == "__main__":
    matrix = [3,2,1,0,4]
    res = Solution().canJump(matrix)
    print res
