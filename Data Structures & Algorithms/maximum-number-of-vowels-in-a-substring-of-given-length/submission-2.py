class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a' : 1, 'e' : 1, 'i' : 1, 'o' : 1, 'u' : 1}
        left = right = 0
        count = maxCount = 0
        while right < len(s):
            if right < k:
                if s[right] in vowels:
                    count += 1
                    maxCount = max(maxCount, count)
                right += 1
            else:
                if s[left] in vowels:
                    count -= 1
                left += 1
                
                if s[right] in vowels:
                    count += 1
                right += 1
                maxCount = max(maxCount, count)
        return maxCount

