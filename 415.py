class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        carry = 0
        p1 = len(num1) -1
        p2 = len(num2) -1
        while p1 >=0 or p2 >=0:
            if p1 >=0:
                val1 = ord(num1[p1])- ord('0')

            else:
                val1 =0
            if p2 >=0:
                val2 = ord(num2[p2])- ord('0')
            else:
                val2 =0
            val= (val1 + val2 + carry) % 10
            carry = ( val1 + val2 + carry)//10
            ans.append(val)
            p1 -=1
            p2 -=1
        if carry:
            ans.append(carry)
        return "".join(str(i) for i in ans[:: -1])

        
