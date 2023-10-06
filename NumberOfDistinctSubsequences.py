class Solution:
    def distinctSubsequences(self, s):
        # Length of the input string
        n = len(s)

        # Initialize an array to store the number of distinct subsequences
        distinct_subsequences_count = [0 if i > 0 else 1 for i in range(n + 1)]

        # Modulus value to prevent integer overflow
        mod = (10**9) + 7

        # Dictionary to store the last occurrence index of each character
        last_occurrence = {}

        # Loop through the characters of the input string
        for i in range(1, n + 1):
            char = s[i - 1]

            # Calculate the number of distinct subsequences for the current character
            distinct_subsequences_count[i] = distinct_subsequences_count[i - 1] * 2 % mod

            # Check if the current character has occurred before
            if char in last_occurrence:
                idx = last_occurrence[char]
                # Subtract the count of subsequences ending with the previous occurrence
                distinct_subsequences_count[i] -= distinct_subsequences_count[idx - 1] % mod

            # Update the last occurrence index of the current character
            last_occurrence[char] = i

        # Return the final count of distinct subsequences modulo the specified value
        return distinct_subsequences_count[n] % mod


solution = Solution()
ans = solution.distinctSubsequences('Hacktoberfest')
print(ans)
