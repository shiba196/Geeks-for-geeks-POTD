class Solution:
    def buildBalancedTree(self,root):
        #code here
        nodes=list()
        def inord(node=root,lst=nodes):
            if not node:
                return
            inord(node.left)
            lst.append(node)
            inord(node.right)
        inord()
        def build(lst):
            if not lst:
                return None
            n=len(lst)
            root=lst[n//2]
            root.left=build(lst[:n//2])
            root.right=build(lst[n//2+1:])
            return root
        return build(nodes)
