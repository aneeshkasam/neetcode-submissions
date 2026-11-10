class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for str in strs:
            charCount = [0] * 26
            for letter in str:
                i = ord(letter) - ord('a')
                charCount[i] += 1
            
            key = tuple(charCount)
            res[key].append(str)

        return list(res.values())
            