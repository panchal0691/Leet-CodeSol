class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        c = Counter()
        
        def isPal():
            one = False
            for k,v in c.items():
                if v%2!=0:
                    if one:
                        return False
                    else:
                        one = True
            return True
        
        def dfs(node):
            if not node:
                return 0
            
            c[node.val]+=1
            if not node.left and not node.right:
                if isPal():
                    c[node.val]-=1
                    return 1
                else:
                    c[node.val]-=1
                    return 0
            res = dfs(node.left)+dfs(node.right)
            c[node.val]-=1
            return res
            
        return dfs(root)
