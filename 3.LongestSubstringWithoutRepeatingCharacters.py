class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # remove till there is no duplciate
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            # only after removing duplicate, we will add s[r]
            charSet.add(s[r])
            # print("r", s[r])
            # print("l", s[l])
            # print(r - l + 1)

            # we will update the result to see if there is max
            res = max(res, r - l + 1)
        return res

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))