class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # left, right = 0, len(s) - 1
        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left, right = left + 1, right - 1

        return s.reverse()


s = ["h", "e", "l", "l", "o"]
solution = Solution()
print(solution.reverseString(s))