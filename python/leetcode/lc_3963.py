class Solution:
    """leetcode 3963. Create Grid With Exactly One Path"""

    def createGrid(self, m: int, n: int) -> list[str]:
        arr = [["#"] * n] * m
        arr[0] = ["."] * n
        for i in range(m):
            arr[i][n - 1] = "."
        return ["".join(row) for row in arr]


if __name__ == "__main__":
    print(Solution().createGrid(2, 3))
