class bst_node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

def insert(root, node):
    if not root:
        root = node
    else:
        if node.value > root.value:
            if root.right == None:
                root.right = node
            else:
                insert(root.right, node)
        elif node.value < root.value:
            if root.left == None:
                root.left = node
            else:
               insert(root.left, node)

def inorder(root, order):
    if root:
        inorder(root.left, order)
        order.append(root.value)
        inorder(root.right, order)
def preorder(root, order):
    if root:
        order.append(root.value)
        preorder(root.left, order)
        preorder(root.right, order)
def postorder(root, order):
    if root:
        postorder(root.left, order)
        postorder(root.right, order)
        order.append(root.value)
        
def levelorder(root, order):
    if root:
        temp = root
        que = []
        while temp:
            order.append(temp.value)
            if temp.left:
                que.append(temp.left)
            if temp.right:
                que.append(temp.right)
            if len(que) > 0:
                temp = que.pop(0)
            else:
                break
    print("level order = ", order)

root = bst_node(50)
insert(root, bst_node(30))
insert(root, bst_node(20))
insert(root, bst_node(40))
insert(root, bst_node(70))
insert(root, bst_node(60))
insert(root, bst_node(80))

nums1 = []
inorder(root, nums1)
print("inorder = ", nums1)
nums1.clear()
preorder(root, nums1)
print("preorder = ", nums1)
nums1.clear()
postorder(root, nums1)
print("postorder = ", nums1)
nums1.clear()
levelorder(root, nums1)