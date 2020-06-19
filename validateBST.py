#THis contain two implementations
### 1. An O(n**2) implementation

def isValidBST1(self, root: TreeNode) -> bool:
    tree_vals = []
    def inorder(root):
        if root:
            inorder(root.left)
            tree_vals.append(root.val)
            inorder(root.right)
        
        for i in range(1, len(tree_vals)):
            if tree_vals[i-1]>=tree_vals[i]:
                return False
        return True
            
            
    return inorder(root)
    
### 2. An O(n) implementation
def isValidBST(self, root):

        if not root:
            return True
            
        stack = [(root, float('-inf'), float('inf')), ] 
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True  