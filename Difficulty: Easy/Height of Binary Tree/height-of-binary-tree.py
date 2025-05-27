'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if root is None:
            return 0
        q=deque([root])
        depth=0
        while q:
            len_q=len(q)
            for _ in range(len_q):
                curr=q.popleft()
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
            depth+=1
        return depth-1
        