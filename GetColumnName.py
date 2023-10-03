class Solution:
    def colName (self, n):
        # your code here
        string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        mapping = dict(zip(range(1,27),string))
        ans = ""
        while n > 0 : 
            rem = n%26
            ans =  mapping.get(rem,'Z') + ans 
            n= n//26 
            if rem == 0:
                n -= 1
            
        return ans  
solution = Solution()
ans = solution.colName(40)
print(ans)
