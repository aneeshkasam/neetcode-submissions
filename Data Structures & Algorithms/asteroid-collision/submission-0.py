class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
            elif asteroid > 0 and stack[-1] > 0:
                stack.append(asteroid)
            elif asteroid < 0 and stack[-1] < 0:
                stack.append(asteroid)
            else:
                compare = stack.pop()
                if asteroid > 0 and compare < 0:
                    stack.append(compare)
                    stack.append(asteroid)
                elif asteroid < 0 and compare > 0:
                    if abs(asteroid) < compare:
                        stack.append(compare)
                    else:
                        while abs(asteroid) > compare and stack:
                            if stack[-1] > 0:
                                compare = stack.pop()
                            else:
                                stack.append(asteroid)
                                break
                        if not stack and abs(asteroid) > compare:
                            stack.append(asteroid)
                        if abs(asteroid) < compare:
                            stack.append(compare)

        return stack