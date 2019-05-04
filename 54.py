class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        #matrix m*n

        ret_list = []
        #get the num of matrix row and matrix column
        row_num = len(matrix)
        if row_num == 0 :
            return ret_list
        column_num = len(matrix[0])

        start_row = 0
        end_row = row_num
        start_column = 0
        end_column = column_num

        while row_num > 0 and column_num > 0:
            for i in range(start_column,end_column,1):
                ret_list.append(matrix[start_row][i])
            row_num -= 1
            start_row += 1
            if row_num*column_num <= 0:
                break
            
            for i in range(start_row,end_row,1):
                ret_list.append(matrix[i][end_column-1])
            column_num -= 1
            end_column -= 1
            if row_num*column_num <= 0:
                break

            for i in range(end_column-1,start_column-1,-1):
                ret_list.append(matrix[end_row-1][i])
            row_num -= 1
            end_row -= 1
            if row_num*column_num <= 0:
                break
            
            for i in range(end_row-1,start_row-1,-1):
                ret_list.append(matrix[i][start_column])
            column_num -= 1
            start_column += 1
            if row_num*column_num <= 0:
                break

        return ret_list


if __name__ == "__main__":
    input_matrix = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
    result = Solution().spiralOrder(input_matrix)
    for i in result:
        print i



