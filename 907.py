class Solution:
    def sumSubarrayMins(self, A):
        n = len(A)
        MOD = 10**9 + 7
        left = [0] * n
        right = [0] * n

        # Left Stack
        Left_st = []
        Left_st.append(0)
        left[0] = 1

        for i in range(1, n):
            while Left_st and A[i] < A[Left_st[-1]]:
                Left_st.pop()

            if not Left_st:
                left[i] = i + 1
            else:
                left[i] = i - Left_st[-1]

            Left_st.append(i)

        # Right Stack
        Right_st = []
        Right_st.append(n - 1)
        right[n - 1] = 1

        for i in range(n - 2, -1, -1):
            while Right_st and A[i] <= A[Right_st[-1]]:
                Right_st.pop()

            if not Right_st:
                right[i] = n - i
            else:
                right[i] = Right_st[-1] - i

            Right_st.append(i)

        # Calculate the result
        res = 0
        for i in range(n):
            prod = (left[i] * right[i]) % MOD
            net = A[i] * prod
            res = (res + net) % MOD

        return res % MOD
