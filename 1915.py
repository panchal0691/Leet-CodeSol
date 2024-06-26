class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mp = {}

        mp[0] = 1
        cum_xor = 0

        result = 0

        for ch in word:
            shift = ord(ch) - ord('a')

            cum_xor ^= (1 << shift)

            result += mp.get(cum_xor, 0)

            for ch1 in range(ord('a'), ord('j') + 1):
                shift = ch1 - ord('a')

                check_xor = (cum_xor ^ (1 << shift))

                result += mp.get(check_xor, 0)

            mp[cum_xor] = mp.get(cum_xor, 0) + 1

        return result
