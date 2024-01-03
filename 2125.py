class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total =0
        prev = 0
        for row in bank:
            c = row.count("1")
            if c >0:
                total += c * prev
                prev = c
        return total
        
