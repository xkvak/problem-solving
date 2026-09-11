from collections import defaultdict


class Solution:
    """leetcode 3483. Unique 3-Digit Even Numbers"""

    # 짝수가 마지막에 올 수 있는 경우의 수 = 짝수의 갯수 * (n - 1) * (n - 2)
    # 문제는 중복인 경우, 202 => 2 * 2 * 1 = 4
    # 짝수를 셀 때에는 중복을 허용하지 않는 다면?
    # 중복을 제외하고 숫자를 센 뒤 중복을 따로 더한다
    def totalNumbers(self, digits: list[int]) -> int:
        ans = 0
        freq = defaultdict(int)
        uniq_even = set()

        for n in digits:
            if n % 2 == 0:
                uniq_even.add(n)
            freq[n] += 1

        for even in uniq_even:
            freq[even] -= 1

            keys = [k for k in freq if freq[k] > 0]
            for i, a in enumerate(keys):
                for b in keys[:i]:
                    # abe
                    if a != 0:
                        ans += 1
                    if b != 0:
                        ans += 1

            for num in keys:
                # aae
                if freq[num] >= 2 and num != 0:
                    ans += 1
            freq[even] += 1

        return ans


if __name__ == "__main__":
    print(Solution().totalNumbers([0, 2, 2]))
