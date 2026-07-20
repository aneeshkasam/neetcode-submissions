class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set()
        finalCount = 0
        count = 0
        for n in nums:
            if n not in hash:
                hash.add(n)

        for n in hash:
            if n - 1 not in hash:
                count = 1
                while(n + 1 in hash):
                    n += 1
                    count += 1
                finalCount = max(finalCount, count)   
        return finalCount         
            


        