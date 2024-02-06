class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(list(word)))
            anagrams[sorted_word].append(word)
        return anagrams.values()
