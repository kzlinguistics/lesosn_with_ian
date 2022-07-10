#awaiting ian to send probelms

#problem sent 
#here is the link 

#https://leetcode.com/problems/path-sum/

print("Problem received")


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], sum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True
        
        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)





