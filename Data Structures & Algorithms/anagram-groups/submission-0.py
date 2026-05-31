class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for n in strs:
            countLetters = [0] * 26
            for m in n:
                countLetters[ord(m) - ord('a')] += 1 #here we are finding the letters number and incrementing the count. the ord() is to get the ascii value
            
            key = tuple(countLetters) # tuple is an unmodifiable list so it can be used as a key unlike a mutable list

            result[key].append(n)
        
        return list(result.values())