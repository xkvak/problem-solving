class Solution:
    """leetcode 2029. Stone Game IX"""

    # 내 턴에 나머지가 1인 값을 낼 경우 -> 상대방도 나머지가 1인 값을 내야 한다 -> 내 턴에 나머지가 2인 값을 낼 경우 -> 상대방도 나머지가 2인 값을 내야 한다 -> ...
    # cnt0 의 갯수가 홀수일 경우 결과가 반전돤다. False 일 때는 3개 부터 반전이 된
    def stomeGameIX(self, stones: list[int]) -> bool:
        cnt = [0] * 3
        for score in stones:
            cnt[score % 3] += 1

        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0
        return abs(cnt[1] - cnt[2]) > 2


if __name__ == "__main__":
    print(Solution().stomeGameIX(stones=[2, 1]))
