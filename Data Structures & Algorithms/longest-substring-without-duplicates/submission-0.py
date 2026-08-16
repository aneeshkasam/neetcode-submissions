class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set()
        finalCount = 0
        left = 0
        for i in range(len(s)):
            if s[i] not in hash:
                hash.add(s[i])
                length = (i - left + 1)
                finalCount = max(finalCount, length)
            else:
                while s[left] != s[i] and left <= i:
                    hash.remove(s[left])
                    left += 1
                left += 1
                length = (i - left + 1)
                finalCount = max(finalCount, length)
        return finalCount