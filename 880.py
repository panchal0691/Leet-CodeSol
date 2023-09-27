class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decoded_length = 0
        

        for char in s:
            if char.isdigit():
                decoded_length *= int(char)
            else:
                decoded_length += 1


        for char in s[::-1]:
            if char.isdigit():
                decoded_length //= int(char)
                k %= decoded_length
            else:
                k %= decoded_length
                if k == 0:
                    return char
                decoded_length -= 1
