class Solution:
    def BoundaryTraversal(self, matrix, n, m):
        if n == 1:
            return matrix[0]
        elif m == 1:
            return [matrix[i][0] for i in range(n)]

        boundary = []

        # Traverse the top row
        boundary.extend(matrix[0])

        # Traverse the rightmost column
        if n > 1:
            boundary.extend(matrix[i][m - 1] for i in range(1, n))

        # Traverse the bottom row if there is more than one row
        if n > 1:
            boundary.extend(matrix[n - 1][m - 2::-1])

        # Traverse the leftmost column if there is more than one column
        if m > 1:
            boundary.extend(matrix[i][0] for i in range(n - 2, 0, -1))

        return boundary

n1 = 3
m1 = 1
matrix1 = [3, 8, 2]

solution = Solution()
ans = solution.BoundaryTraversal(matrix1, n1, m1)
print(ans)


