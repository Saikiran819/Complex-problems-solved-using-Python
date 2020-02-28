class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.left.left = Node(9)
root.left.left.left.right = Node(10)

def zigzag_traversal(root):
    
    if root:
        stack1 = []
        stack2 = []
        ltr = True
        stack1.append(root)
    while len(stack1) > 0:
        item = stack1.pop()
        print(item.value)
        if ltr:
            if item.left:
                stack2.append(item.left)
            if item.right:
                stack2.append(item.right)
        else:
            if item.right:
                stack2.append(item.right)
            if item.left:
                stack2.append(item.left)
        if len(stack1) == 0:
            ltr = not ltr
            stack1, stack2 = stack2, stack1

zigzag_traversal(root)