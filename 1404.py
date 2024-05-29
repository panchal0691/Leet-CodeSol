class Solution:
    def addOne(self, s: str) -> str:
        s_list = list(s)
        i = len(s_list) - 1

        while i >= 0 and s_list[i] != '0':
            s_list[i] = '0'
            i -= 1

        if i < 0:
            s_list.insert(0, '1')
        else:
            s_list[i] = '1'
        
        return ''.join(s_list)

    def numSteps(self, s: str) -> int:
        op = 0

        while len(s) > 1:
            if s[-1] == '0':
                s = s[:-1]
            else:
                s = self.addOne(s)
            op += 1

        return op
