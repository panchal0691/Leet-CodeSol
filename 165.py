class Solution:
    def getTokens(self, version: str) -> List[str]:
        version_tokens = version.split('.')
        return version_tokens

    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = self.getTokens(version1)
        v2 = self.getTokens(version2)

        m = len(v1)
        n = len(v2)

        i = 0
        while i < m or i < n:
            a = int(v1[i]) if i < m else 0
            b = int(v2[i]) if i < n else 0

            if a > b:
                return 1
            elif b > a:
                return -1
            else:
                i += 1

        return 0
