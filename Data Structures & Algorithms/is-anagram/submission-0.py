class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        freqt = {}
        if len(s) != len(t):
            return False


        for ch in s:
            if ch in freqs:
                freqs[ch] += 1
            else:
                freqs[ch] = 1
        for ch in t:
            if ch in freqt:
                freqt[ch] += 1
            else:
                freqt[ch] = 1

        for ch in freqs:
            if ch not in freqt or freqs[ch] != freqt[ch]:
                return False

        return True
        