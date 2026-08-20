class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        result = 0
        left = 0

        for right in range(len(s)):
            map[s[right]] = 1 + map.get(s[right], 0)

            while (right - left + 1) - max(map.values()) > k:
                map[s[left]] -= 1
                left += 1
            result = max(result, (right - left + 1))
        return result