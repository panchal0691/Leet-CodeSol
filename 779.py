class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n ==1: return 0
        parent = self.kthGrammar(n-1,k/2 + k%2)
        isKOdd = k%2 ==1
        if parent ==1: 
            return 1 if isKOdd else 0
        else:
            return 0 if isKOdd else 1


The given code uses a recursive approach to find the value at a specific index in a binary sequence. Let's analyze its time and space complexity:

**Time Complexity:**
The time complexity of the code can be analyzed in terms of the number of recursive calls made. In each recursive call, the code reduces the problem size by moving to the previous level of the binary sequence (from n to n-1). At each level, it performs a constant amount of work to determine the value at the current index.

The recursion goes down to level 1, so there will be O(n) recursive calls. At each level, a constant amount of work is performed (e.g., calculating the parent value and performing basic arithmetic operations). Therefore, the time complexity of the code is O(n).

**Space Complexity:**
The space complexity is determined by the depth of the recursion and the auxiliary space used by the function call stack. Since there can be up to n recursive calls (corresponding to the depth of the binary tree), the space complexity is O(n).

In summary, the time complexity is O(n), and the space complexity is O(n) due to the recursive function calls. The code uses a recursive approach to traverse a binary tree-like structure to find the value at the given index by calculating parent values and making decisions based on the current and parent values.
