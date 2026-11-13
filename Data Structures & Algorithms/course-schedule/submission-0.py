class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for (course,prereq) in prerequisites:
            graph[course].append(prereq)
        
        visited = set()
        completed = set()
        def dfs(graph, course):
            if course in completed:
                return True
            if course in visited:
                return False

            stack = [(course, False)]
            while stack:
                node, done = stack.pop()
                if done:
                    visited.remove(node)
                    completed.add(node)
                    continue

                if node in completed:
                    continue

                if node in visited:
                    return False

                visited.add(node)
                stack.append((node, True))
                for prereq in (graph[node]):
                    stack.append((prereq, False))
            return True

        for i in range(numCourses):
            if not dfs(graph, i):
                return False

        return True
