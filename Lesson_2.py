#awaiting ian to send probelms

#problem sent 
#here is the link 

#https://leetcode.com/problems/path-sum/

#YT link: https://www.youtube.com/watch?v=Dhd-qxWQBAQ

print("Problem received")


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], sum: int) -> bool:

        #we want to call our function recursively
        #hence the last line tbh
        
        #if not root. you need to get false because you need to stop at root. 
        if not root:
            return False

        #when there is no longer a child here, stop 

        ########
        #question 1- how do I know this is going to work and keep updating. there is not 
        #for loop here. Is it being driven by the last line? 

        #answer from myself- yes 


        ########
        sum -= root.val 
        #we just keep updating the sum 

        #this is to look for the leaf 
        #this is an "iterative" solution. I need to stop thinking about the first pass 

        #this is to check if the root has a root to leaf path that leads to 0 
        
        if not root.left and not root.right:

            #once we hit our leaf node, we want to see if our "sum" is 0 
            return sum == 0 
        
        #the tree you are searching for need to have a value that is 
        #smaller than the one you start the root with. 

        #if it does not equal. you have to keep on going. the magic of CS 

        #you are making progress at every step 
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)





