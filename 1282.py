class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = collections.defaultdict(collections.deque)

        for i, s in enumerate(groupSizes):
            groups[s].append(i)


        def break_into_groups(arr,s):
            r= []
            current= []


            for i,x in enumerate(arr):
                current.append(x)
                if (i+1)% s ==0:
                    r.append(current)
                    current =  []

            return r

        ans = []
        for s in groups.keys():
            for g in break_into_groups(groups[s],s ):
                ans.append(g)

        return ans
        
