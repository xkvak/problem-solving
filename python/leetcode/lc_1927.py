class Solution:
    """leetcode 1927. Sum Game"""

    # ?가 홀수 일 경우 승리할 수 없다
    # ?가 짝수 일 경우 (? / 2) * 9
    # ?6?6 0003
    def sumGame(self, num: str) -> bool:
        n = len(num)
        diff = 0
        cnt = 0
        for i in range(n):
            if num[i] == "?":
                cnt += 1
            elif i < n // 2:
                diff += int(num[i])
            else:
                diff -= int(num[i])

        if cnt % 2:
            return True

        left_cnt = num[: n // 2].count("?")
        right_cnt = cnt - left_cnt
        return diff != 9 * (right_cnt - left_cnt) // 2


if __name__ == "__main__":
    print(Solution().sumGame("5023"))
