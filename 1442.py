class Solution:
    def countTriplets(self, arr):
        # Create a prefix XOR array with an initial zero
        prefixXor = [0] + arr[:]
        n = len(prefixXor)

        # Compute the prefix XOR values
        for i in range(1, n):
            prefixXor[i] ^= prefixXor[i - 1]

        triplets = 0

        # Count the triplets
        for i in range(n):
            for k in range(i + 1, n):
                if prefixXor[k] == prefixXor[i]:
                    triplets += k - i - 1

        return triplets
