# n = 4 
# m = 4
# matrix = [[1, 2, 3, 4],
#          [5, 6, 7, 8],
#          [9, 10, 11, 12],
#          [13, 14, 15,16]]
# l = []
# for i in range(m):
#     l.append(matrix[0][i])
# for i in range(1,n):
#     l.append(matrix[i][m-1])
# for i in range(m-2,-1,-1):
#     l.append(matrix[-1][i])
# for i in range(n-2,0,-1):
#     l.append(matrix[i][0])
# print(l)
# for i in l:
#     print(i,end=' ')

n1 = 3
m1 = 1
matrix1 = [3,8,2]

class Solution:
    def BoundaryTraversal(self, matrix, n, m):
        if n == 1:
            return matrix[0]
        elif m == 1:
            return [matrix[i][0] for i in range(n)]

        boundary = []

        # Traverse the top row
        for i in range(m):
            boundary.append(matrix[0][i])

        # Traverse the rightmost column
        for i in range(1, n):
            boundary.append(matrix[i][m - 1])

        # Traverse the bottom row if there is more than one row
        if n > 1:
            for i in range(m - 2, -1, -1):
                boundary.append(matrix[n - 1][i])

        # Traverse the leftmost column if there is more than one column
        if m > 1:
            for i in range(n - 2, 0, -1):
                boundary.append(matrix[i][0])

        return boundary

solution = Solution()
ans = solution.BoundaryTraversal(matrix1,n1,m1)
print(ans)
