#
# DO NOT FORGET TO ADD COMMENTS
#

from stack import Stack

class BinaryTree:
    def __init__(self,rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s

class ExpTree(BinaryTree):

    def make_tree(postfix):     # Followed Michaels Pseudo Code
        stack = Stack()
        for i in postfix :
            if i in ('*/+-^') :
                node = ExpTree(i)
                
                num1 = stack.pop()
                num2 = stack.pop()

                if isinstance (num1, ExpTree) :
                    node.rightChild = num1
                else :
                    node.insertRight(num1)

                if isinstance (num2, ExpTree) :
                    node.leftChild = num2
                else :
                    node.insertLeft(num2)
                    
                stack.push(node)
            else :
                node = ExpTree(i)
                stack.push(node)

        output = stack.pop()
        return(output)
    
    def preorder(self, tree): # this goes middle left right 
        s = ''
        if ExpTree.getRightChild(tree) == None and ExpTree.getLeftChild(tree) == None:
            center = ExpTree.getRootVal(tree)
            s = center 
        else:
            left = self.preorder(ExpTree.getLeftChild(tree))
            center = ExpTree.getRootVal(tree)
            right = self.preorder(ExpTree.getRightChild(tree))
            s = center + left + right 
        
        return s

    def inorder(self, tree): # this goes left middle right 
        s = ''
        if ExpTree.getRightChild(tree) == None and ExpTree.getLeftChild(tree) == None:
            center = ExpTree.getRootVal(tree)
            s = center 
        else:
            left = self.inorder(ExpTree.getLeftChild(tree))
            center = ExpTree.getRootVal(tree)
            right = self.inorder(ExpTree.getRightChild(tree))
            
            if center in '*/+-^' :
                left = ('(' + left)
                right = (right + ')')
                s = left + center + right
            else :
                s = left + center + right 
        
        return s
      
    def postorder(self, tree): # this goes left right middle 
        s = ''
        if ExpTree.getRightChild(tree) == None and ExpTree.getLeftChild(tree) == None:
            center = ExpTree.getRootVal(tree)
            s = center 
        else:
            left = self.postorder(ExpTree.getLeftChild(tree))
            center = ExpTree.getRootVal(tree)
            right = self.postorder(ExpTree.getRightChild(tree))
            s = left + right + center 
        
        return s

    def evaluate(self, tree):       # Citing: Michaels Pseudo Code for help during May/23 zoom session 
        if ExpTree.getRootVal(tree) not in ('*/+-^'):
            return ExpTree.getRootVal(tree)
        else:
            node = ExpTree.getRootVal(tree)
            left = float(self.evaluate(ExpTree.getLeftChild(tree)))
            right = float(self.evaluate(ExpTree.getRightChild(tree)))

            if node == '*' :
                return  left * right
            elif node == '/' :
                return  left / right
            elif node == '-' :
                return  left - right
            elif node == '+' :
                return  left + right
            elif node == '^' :
                return left ** right 
                                
        
            
    def __str__(self):
        return self.inorder(self)
   
# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':

    # test a BinaryTree
    
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'
    
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'

    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    
    # test an ExpTree
    
    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5+(2*3))'
    assert tree.inorder(tree) == '(5+(2*3))'
    assert tree.postorder(tree) == '523*+'
    assert tree.preorder(tree) == '+5*23'
    assert tree.evaluate(tree) == 11.0

    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert tree.inorder(tree) == '((5+2)*3)'
    assert tree.postorder(tree) == '52+3*'
    assert tree.preorder(tree) == '*+523'
    assert tree.evaluate(tree) == 21.0
    
    
