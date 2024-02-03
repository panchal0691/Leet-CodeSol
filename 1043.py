 n = len(arr)
        t = [0] * (n + 1)

        # t[i] = Maximum sum for the partition arr of size i
        # we need to find max for the whole array = t[n]
        for i in range(1, n + 1):  # size of array is i
            currMax = -1

            for j in range(1, k + 1):  # I am taking a subarray of size j
                if i - j >= 0:
                    currMax = max(currMax, arr[i - j])
                    t[i] = max(t[i], t[i - j] + currMax * j)

        return t[n]
