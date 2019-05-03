class Solution(object):
    #binary search
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        low_num , high_num = 0, x
        mid_num = (low_num + high_num) // 2
        while  mid_num > x // mid_num or (mid_num + 1) <= x // (mid_num+1):
            if mid_num > x // mid_num:
                high_num = mid_num
            else:
                low_num = mid_num
            mid_num = (low_num + high_num) / 2
        return mid_num





if __name__ == "__main__":
    res = Solution().mySqrt(8)
    print res