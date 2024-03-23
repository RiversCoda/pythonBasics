class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        l = [[1]]
        for i in range(1, numRows):
            row = [1]  # 每行的第一个元素总是1
            for j in range(1, i):
                row.append(l[i - 1][j - 1] + l[i - 1][j])  # 上一行的相邻两个元素之和
            row.append(1)  # 每行的最后一个元素总是1
            l.append(row)
        return l
