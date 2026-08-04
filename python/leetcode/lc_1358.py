class Solution:
    """ leetcode 1358. Number of Substrings Containing All Three Characters """

    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        INF = n
        next_pos = {c: [INF] * (n + 1) for c in 'abc'}
        for i in range(n - 1, -1, -1):
            for c in 'abc':
                next_pos[c][i] = next_pos[c][i + 1]
            next_pos[s[i]][i] = i

        ans = 0
        for i in range(n):
            j = max(next_pos['a'][i], next_pos['b'][i], next_pos['c'][i])
            if j < n:
                ans += n - j

        return ans

if __name__ == "__main__":
    print(Solution().numberOfSubstrings("aaacb"))
