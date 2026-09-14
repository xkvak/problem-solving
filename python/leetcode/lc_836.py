class Solution:
    """leetcode 836. Rectangle Overlap"""

    # 겹친다란 무엇인가
    # x1~x2 사이에 값이 있으면서 y1~y2 사이에 있어야 한다.
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x_overlap = max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])
        y_overlap = max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])
        return x_overlap and y_overlap


if __name__ == "__main__":
    print(Solution().isRectangleOverlap(rec1=[0, 0, 2, 2], rec2=[1, 1, 3, 3]))
