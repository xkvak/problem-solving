class Solution:
    """ leetcode 3731. Find Missing Elements """

    def findMissingElements(self, nums: list[int]) -> list[int]:
        min_num, max_num = min(nums), max(nums)
        visited = set(nums)
        ans = []
        for n in range(min_num + 1, max_num):
            if n not in visited:
                ans.append(n)

        return ans

if __name__ == "__main__":
    print(Solution().findMissingElements([7,8,6,9]))
