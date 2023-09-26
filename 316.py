# Format one
from sortedcontainers import SortedSet
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        N = len(s)
        allc = SortedSet(s)
        A = len(allc)
        indices = collections.defaultdict(list)
        for i,x in enumerate(s):
            indices[x].append(i)

        def good(c):
            first_index = bisect.bisect_left(indices[c]  , current)
            first = indices[c][first_index]

            for x in allc:
                index = bisect.bisect_left(indices[x] , first)
                if not (0 <= index < len(indices[x])):
                    return False
            return True
        ans = []
        current = 0

        while len(ans) < A:
            for c in allc:
                if good(c):
                    allc.remove(c)
                    ans.append(c)
                    index = bisect.bisect_left(indices[c] , current)
                    current = indices[c][index] +1
                    break
        return "".join(ans)





# Format two
from sortedcontainers import SortedSet
import bisect
import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        string_length = len(s)
        unique_chars = SortedSet(s)
        num_unique_chars = len(unique_chars)
        char_indices = collections.defaultdict(list)

        for i, char in enumerate(s):
            char_indices[char].append(i)

        def is_good(char):
            first_index = bisect.bisect_left(char_indices[char], current)
            first = char_indices[char][first_index]

            for x in unique_chars:
                index = bisect.bisect_left(char_indices[x], first)
                if not (0 <= index < len(char_indices[x])):
                    return False
            return True
        
        result = []
        current = 0

        while len(result) < num_unique_chars:
            for char in unique_chars:
                if is_good(char):
                    unique_chars.remove(char)
                    result.append(char)
                    index = bisect.bisect_left(char_indices[char], current)
                    current = char_indices[char][index] + 1
                    break

        return "".join(result)
