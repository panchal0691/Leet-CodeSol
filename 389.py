class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # l2 = [*s]
        # l1 = [*t]
        # temp3 = []
        # for element in l1:
        #     if element not in l2:
        #         temp3 = element 
 
        # return temp3
        return list((collections.Counter(t) - collections.Counter(s)).keys())[0]
