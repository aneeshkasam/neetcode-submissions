class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        map = defaultdict(int)
        atmostTypes = 0
        Fruits = 0
        left = right = 0
        maxFruits = 0
        while right < len(fruits):
            if map[fruits[right]] == 0:
                atmostTypes += 1

            if atmostTypes <= 2:
                map[fruits[right]] += 1
                right += 1
                Fruits += 1
                maxFruits = max(maxFruits, Fruits)
            else:
                while atmostTypes > 2:
                    map[fruits[left]] -= 1
                    Fruits -= 1
                    if map[fruits[left]] == 0:
                        left += 1
                        atmostTypes -= 1
                        map[fruits[right]] += 1
                        right += 1
                        Fruits += 1
                    else:
                        left += 1
                        
        return maxFruits