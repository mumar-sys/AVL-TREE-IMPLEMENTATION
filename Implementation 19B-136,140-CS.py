# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 17:49:28 2021

@author: intel
"""

## Section CS(B)
## Group No: 11
## MUHAMMAD UMAR "19B-136-CS"
## SYED MUHAMMAD ZAID "19B-140-CS"
## AVl_Obj TREE IMPLEMENTATION
## GITHUB LINK: 

##########
class AVl_Node: 
    def __init__(self,data): 
        self.data = data
        self.left = None  ## hold the information of left node  
        self.right = None  ## hold the information of right node
        self.height = 1  ## Assign the height of 1 to every node 
        
class AVl_Tree:
    def __init__(self):
        self.root=None
        
    def AVl_Height(self,root): 
        if root is None:
       # if not root:
            return 0  ## no node in the AVl_Obj tree
        return root.height ## return the height of the root
    
    
    #it is just maintaing the balance of every node with its respective formula.
    def Balance_Calculator(self, root): 
        if root is None:
        #if not root:
            return "No Node, so balance factor is zero"
        return self.AVl_Height(root.left) - self.AVl_Height(root.right)
    
    def leftleftRotation(self,temp):
        temp1 = temp.right 
        temp2 = temp1.left 
  
        ## Rotating left 
        temp1.left = temp 
        temp.right = temp2 
  
        ## Update heights
        ## Update the height of child node of the root noode
        temp.height = 1 + max(self.AVl_Height(temp.left), self.AVl_Height(temp.right))
        ## Update the height of the child node of the previous child node
        temp1.height = 1 + max(self.AVl_Height(temp1.left), self.AVl_Height(temp1.right)) 
  
        ## As rotation is done and the root is changed so new root should be returned 
        return temp1
    
    def RightRightRotation(self,temp):
        temp1 = temp.left 
        temp2 = temp1.right 
  
        ## rotating right 
        temp1.right = temp 
        temp.left = temp2 
  
        ## Update heights
        ## Update the height of the child node of the root node
        temp.height = 1 + max(self.AVl_Height(temp.left), self.AVl_Height(temp.right))
        ## Update the height of the child node of the previous child node
        temp1.height = 1 + max(self.AVl_Height(temp1.left), self.AVl_Height(temp1.right)) 
  
        # As rotation is done and the root is changed so new root should be returned 
        return temp1 
             
    def AVl_insert(self,root,key):
        ## First Implementing basic BST Insert
        if root is None:
            root = AVl_Node(key)  ## for empty tree make the inserted node as root
        
        elif key < root.data:
            root.left = self.AVl_insert(root.left,key) ## if key is less than root traverse the left tree recursively
            
        else:
            root.right = self.AVl_insert(root.right,key) ## if key is greater than root travers the right sub tree recursively

        ## Update the height of previous node after insertion of every  new node
        root.height = 1 + max(self.AVl_Height(root.left), self.AVl_Height(root.right))
        
        ## calculate balance factor after insertion of every node
        Calc_balance = self.Balance_Calculator(root)
        
        ## Now if balance factor is other than -1,0,1 
        ## Check the condition of rotation and perform the obligatory rotation
        if Calc_balance < -1 and key > root.right.data: 
            return self.leftleftRotation(root)
        ## This means an ascending order is implemented in tree so left left rotation to be used
        
        
        if Calc_balance > 1 and key < root.left.data:
            return self.RightRightRotation(root)
        ## This means descending order is implemeted in tree so right right rotation to be used
            
        if Calc_balance > 1 and key > root.left.data: 
            root.left = self.leftleftRotation(root.left) ## giving a left rotation first
            return self.RightRightRotation(root)
        ## if a node has a element in the left and then in the right and balance factor gretae than 1 then left right rotation is used
        
        if Calc_balance < -1 and key < root.right.data: 
            root.right = self.RightRightRotation(root.right) ## giving a right rotation first
            return self.leftleftRotation(root)  ##left
        ## if a node has a element in the right and then in the left and balance fatcor  less tha -1 then right left rootation is used
        
        return root
    

    def AVL_Search(self,root,Value):
       # node=self.root
        
        # if node is None which is a starting point for searching it will run this condition and make exit due to 'return'.
        if root is None:
            return False
        
        #it will simply return in boolean TRUE or FALSE we found through the search function.
        elif Value==root.data:
            return True
        
        
        #if the search value is greater than the root value then definitely a right tree will be call recursively.
        elif Value > root.data:
            return self.AVL_Search(root.right, Value)
        
        #or if the search value is lesser than the root value then a left tree will be called recursively. 
        elif Value < root.data:
           return self.AVL_Search(root.left, Value)
           
        return False
    
    # this function is just running on the left side of tree to find the minimum value for Successor.
    def AVL_Minimum(self,root):
        while root.left !=  None:
            root = root.left
        return root.data

    
    # this function is just running on the right side of tree to find the maximum value for Predecessor.
    def AVL_Maximum(self,root):
        while root.right != None:
            root=root.right
        return root.data
    
    # successor is finding the minimum value on the right side recursively of tree which probably be the left-most in right tree.
    def Successor(self,root):
        while root.right != None:
            x=self.AVL_Minimum(root.right)
            return x
        
    # predecessor is finding the maximum value on the left side recursively of tree.
    def Predecessor(self,root):
        while root.left != None:
            x=self.AVL_Maximum(root.left)
            return x
        
    # here key is what you are going to delete.
    def AVL_Delete(self,root,key):
        # we are checking whether the root is none or not.
        if root is None:
            return None
        # if the given key is less then root's value then call a delete function recursively on a left tree.
        elif key < root.data:
            root.left=self.AVL_Delete(root.left, key)
        # if the given key is greater then root's value then call a delete function recursively on a right tree.
        elif key > root.data:
            root.right=self.AVL_Delete(root.right, key)
        
        # after finding all we have to do is to delete that node so,
        
        else:
            #CASE1: it has no child either on its left or right,
            if root.left is None and root.right is None:
                root=None
                return
            
        
            #CASE2: it has one child either on its left or right so case2 itself contain 2 conditions.
            elif root.left is None: 
                x=root
                root=root.right
                root=None
                return x
            
            elif root.right is None:
                x=root
                root=root.left
                root=None
                return x
        
            #CASE3: When it has 2 childs.
            else:
                x=self.AVL_Minimum(root.right)
                x.data=root.data
                root.right = self.AVL_Delete(root.right, x.data)
                temp = self.AVL_Minimum(root.right) 
                root.data = temp.data 
                root.right = self.AVL_Delete(root.right, temp.data)           
                
        if root is None:
            return None
        ## Update the height of previous node after insertion of every  new node  
        root.height=1 + max(self.AVl_Height(root.left),self.AVl_Height(root.right))
        
        ## calculate balance factor after insertion of every node
        Calc_balance=self.Balance_Calculator(root)
        
        ## Now Again check  balance factor is other than -1,0,1 
        ## Check the condition of rotation and perform the obligatory rotation
        if Calc_balance < -1 and key > root.right.data:   
              return self.leftleftRotation(root)
        ## This means an ascending order is implemented in tree so left left rotation to be used
        
        if Calc_balance > 1 and key < root.left.data:
            return self.RightRightRotation(root)
        ## Now it will give rotation to the elements which are right heavy
        
        ## Left right rotation
        if Calc_balance > 1 and key > root.left.data: 
            root.left = self.leftleftRotation(root.left) 
            return self.RightRightRotation(root)
        
        ## right left rotation
        if Calc_balance < -1 and key < root.right.data: 
            root.right = self.RightRightRotation(root.right) 
            return self.leftleftRotation(root)  
        return root
    
    
# 1 PRINT METHOD    
    # here we are printing our tree in preorder format which is RLR (root,left,right) so,
    def preorder(self,root):
        x=[]
    # it will recursivley run for left and right and append the data in x starting from root.
        if root is not None:
            x.append(root.data)
            x=x+self.preorder(root.left)
            x=x+ self.preorder(root.right)
        return x
    

    ## AVL Tree general implementation
    ## Can sort the data in O(lg*n)
    ## Basically in order traversal
    def AVL_Implementation(self,root):
        # appending all the print values here in x.
        x = []
        if root is not None:
            x = self.AVL_Implementation(root.left) ## traversing the left side of root node
            x.append(root.data) 
            x = x + self.AVL_Implementation(root.right) ## traversing the right side of root node
        return x



## Main Function Driver Code        
Tree = AVl_Tree() 
root = None 
root = Tree.AVl_insert(root, 2) 
root = Tree.AVl_insert(root, 86) 
root = Tree.AVl_insert(root, 60) 
root = Tree.AVl_insert(root, 50) 
root = Tree.AVl_insert(root, 70)
root = Tree.AVl_insert(root, 8)
root = Tree.AVl_insert(root, 99)
print("Tree after first insertion:")
print(Tree.preorder(root))
root=Tree.AVL_Delete(root,70)
root=Tree.AVL_Delete(root, 2)
print("Tree after first deletion:")
print(Tree.preorder(root))
root=Tree.AVl_insert(root,34)
root=Tree.AVl_insert(root, 72)
root=Tree.AVl_insert(root, 11)
root=Tree.AVl_insert(root, 87)
print("Tree After second insertion:")
print(Tree.preorder(root))
root=Tree.AVL_Delete(root, 72)
root=Tree.AVL_Delete(root, 99)
print("Final Tree::")
print(Tree.preorder(root))


## Complementary Function Driver Code
print("value found in avl tree: ",Tree.AVL_Search(root, 10000))
print("value found in avl tree: ",Tree.AVL_Search(root, 87))
print("Minimum value in the tree is: ",Tree.AVL_Minimum(root))
print("Successor of the tree is: ",Tree.Successor(root))
print("Predecessor of the tree is: ",Tree.Predecessor(root))
print("Maximum value in the tree is: ",Tree.AVL_Maximum(root))

        
## AVL Application Driver Code        
print("Sorted: ",Tree.AVL_Implementation(root))        
        
#################    END #####################################
