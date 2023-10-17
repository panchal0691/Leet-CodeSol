from typing import List

class Solution:
    def validateBinaryTreeNodes(self, N: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0] * N
        edges = 0

        for x in leftChild + rightChild:
            if x != -1:
                indegree[x] += 1
                edges += 1

        if edges != N - 1:
            return False

        def get_root():
            for i, x in enumerate(indegree):
                if x == 0:
                    return i
            return -1

        root = get_root()
        if root == -1:
            return False

        seen = set()

        def recurse(x):
            if x in seen:
                return
            if x == -1:
                return

            seen.add(x)
            recurse(leftChild[x])
            recurse(rightChild[x])

        recurse(root)

        if len(seen) != N:
            return False

        return True
