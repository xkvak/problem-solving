from collections import Counter


class Solution:
    """leetcode 835. Image Overlap"""

    def largestOrverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        a = [(y, x) for y, row in enumerate(img1) for x, v in enumerate(row) if v]
        b = [(y, x) for y, row in enumerate(img2) for x, v in enumerate(row) if v]
        cnt = Counter((y1 - y2, x1 - x2) for y1, x1 in a for y2, x2 in b)
        return max(cnt.values(), default=0)


if __name__ == "__main__":
    print(
        Solution().largestOrverlap(
            img1=[[1, 1, 0], [0, 1, 0], [0, 1, 0]],
            img2=[[0, 0, 0], [0, 1, 1], [0, 0, 1]],
        )
    )
