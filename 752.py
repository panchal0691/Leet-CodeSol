from collections import deque

class Solution:
    def fillNeighbors(self, que, curr, dead):
        for i in range(4):
            ch = curr[i]

            dec = str(int(ch) - 1) if ch != '0' else '9'
            inc = str(int(ch) + 1) if ch != '9' else '0'

            curr_list = list(curr)
            curr_list[i] = dec
            new_curr_dec = ''.join(curr_list)
            if new_curr_dec not in dead:
                dead.add(new_curr_dec)
                que.append(new_curr_dec)

            curr_list[i] = inc
            new_curr_inc = ''.join(curr_list)
            if new_curr_inc not in dead:
                dead.add(new_curr_inc)
                que.append(new_curr_inc)

    def openLock(self, deadends, target):
        dead = set(deadends)
        
        start = "0000"
        if start in dead:
            return -1
        
        que = deque([start])
        level = 0
        
        while que:
            n = len(que)
            for _ in range(n):
                curr = que.popleft()
                if curr == target:
                    return level
                
                self.fillNeighbors(que, curr, dead)
            
            level += 1
        
        return -1
