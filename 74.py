
class Solution(object):
    # search the targe in high efficiency
    # binary search
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row_num = len(matrix)
        column_num = len(matrix[0])
        start_loc = 0
        end_loc = column_num * row_num-1

        while start_loc <= end_loc:
            mid_loc = (start_loc + end_loc) / 2
            # print start_loc, end_loc, mid_loc
            # print mid_loc / row_num
            # print mid_loc % row_num
            mid_num = matrix[mid_loc / column_num][mid_loc % column_num]
            if mid_num < target:
                start_loc = mid_loc +1
                continue
            elif mid_num > target:
                end_loc = mid_loc -1
                continue
            elif mid_num == target:
                return True


if __name__ == "__main__":
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 13
    res = Solution().searchMatrix(matrix, target)
    print res
