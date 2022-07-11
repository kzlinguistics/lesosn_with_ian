#awaiting ian to send probelms

#problem sent 
#here is the link 

#https://leetcode.com/problems/path-sum/

print("Problem received")


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], sum: int) -> bool:
        
        #if not root. you need to get false because you need to stop at root. 
        if not root:
            return False


        #this is to look for the leaf 
        if not root.left and not root.right and root.val == sum:
            return True
        
        #the tree you are searching for need to have a value that is 
        #smaller than the one you start the root with. 

        #remember the example Youtube, If the goal is 22, the root is 5. The "sum"
        #should be 17 

        sum -= root.val


        #if it does not equal. you have to keep on going. the magic of CS 
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)





