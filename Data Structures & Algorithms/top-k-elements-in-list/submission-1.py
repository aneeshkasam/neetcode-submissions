class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dup = {}
        dup1 = []
        result = []
        a = 0
        max = k
        for n in nums:
            if n not in dup:
                dup[n] = 1
            else:
                dup[n] += 1
        while(max > 0):
            for n in dup:
                if(a < dup[n]):
                    a = dup[n] 
            for n in dup:
                if dup[n] == a:
                    result.append(n)
                    dup[n] = 0
                    a = 0
                    max -= 1
                    break

        return result