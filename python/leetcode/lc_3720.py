from matplotlib.pyplot import flag


class Solution:
    """leetcode 3720. Lexicographically Smallest Permutation Greater Than Target"""

    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(target)
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        best_pos, best_ch, best_freq = -1, -1, []
        i = 0
        while i < n:
            order = ord(target[i]) - ord('a')
            for nxt in range(order + 1, 26):
                if freq[nxt] > 0:
                    best_pos, best_ch, best_freq = i, nxt, freq[:]
                    break
            if freq[order]:
                freq[order] -= 1
                i += 1
            else:
                break

        if best_pos == -1:
            return ""
        
        ans = list(target[:best_pos] + chr(best_ch + ord('a')))
        best_freq[best_ch] -= 1
        for ch in range(26):
            ans += [chr(ch + ord('a'))] * best_freq[ch]
            
        return "".join(ans)


if __name__ == "__main__":
    print(Solution().lexGreaterPermutation(s = "ab", target = "ab"))
