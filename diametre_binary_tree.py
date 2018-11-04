
class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

def height(root,ans):
    if root == None:
        return 0
    left_height = height(root.left,ans)
    right_height = height(root.right,ans)

    print "inside",left_height,right_height
    ans = max(ans,left_height+1+right_height)

    return (1+max(left_height,right_height))

def diameter(root):
    if root==None:
        return 0

    ans = -111
    tree_height = height(root,ans)
    return tree_height
    


def printTree(root):
    
    if root==None:
        return

    printTree(root.left)
    print root.data
    printTree(root.right)

    return

def main():

    root = Node(1)
    root.left = Node(2);
    root.right = Node(3);
    root.left.left = Node(4);
    root.left.right = Node(5);
    
    printTree(root)
    l = diameter(root)
    print "longest path: ",l

main()
