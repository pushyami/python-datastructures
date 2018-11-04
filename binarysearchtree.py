class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data
    
def main():

    root = Node(10)
    root.insert(4)
    root.insert(6)
    root.insert(12)
    root.insert(15)

    root.PrintTree()

main()
