# pylint: disable=too-few-public-methods
class Solution:
    """leetcode 120. Triangle"""

    def minimumTotal(self, triangle: list[list[int]]) -> int:
        curr_row = [0]

        for i, row in enumerate(triangle):
            nxt_row = []
            for j, val in enumerate(row):
                if j == 0:
                    nxt_row.append(curr_row[j] + val)
                elif j == i:
                    nxt_row.append(curr_row[j - 1] + val)
                else:
                    nxt_row.append(min(curr_row[j], curr_row[j - 1]) + val)

            curr_row = nxt_row

        return min(curr_row)


if __name__ == "__main__":
    print(Solution().minimumTotal([[-1], [3, 2], [1, -2, -1]]))
