#1.---BST In,Pre,Post(recursion)---
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)



def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)



def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")



root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.right = Node("F")


print("Inorder:")
inorder(root)

print("\nPreorder:")
preorder(root)

print("\nPostorder:")
postorder(root)





#2 ---IterativeTraversal(stack)----

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Iterative Inorder
def inorder(root):
    stack = []
    result = []

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        result.append(root.data)
        root = root.right

    return result



def preorder(root):
    if root is None:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.data)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return result



def postorder(root):
    if root is None:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.data)

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    return result[::-1]



root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.right = Node("F")


print("Inorder:", inorder(root))
print("Preorder:", preorder(root))
print("Postorder:", postorder(root))


#3.---CountingNodes-Total,leaf&Internal---


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count(root):
    if root is None:
        return 0, 0, 0

    total = 1

    if root.left is None and root.right is None:
        leaf = 1
        internal = 0
    else:
        leaf = 0
        internal = 1

    t1, l1, i1 = count(root.left)
    t2, l2, i2 = count(root.right)

    return (total + t1 + t2,
            leaf + l1 + l2,
            internal + i1 + i2)



root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.right = Node("F")


total, leaf, internal = count(root)

print("Total Nodes:", total)
print("Leaf Nodes:", leaf)
print("Internal Nodes:", internal)


#4.---Min&MaxBinaryTree----

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_min_max(root):
    if root is None:
        return None, None

    minimum = root.data
    maximum = root.data

    stack = [root]

    while stack:
        node = stack.pop()

        minimum = min(minimum, node.data)
        maximum = max(maximum, node.data)

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    return minimum, maximum



root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.right = Node(80)


minimum, maximum = find_min_max(root)

print("Minimum:", minimum)
print("Maximum:", maximum)


#5---BST & Searching---

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root



def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)



root = None

for value in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, value)


# Search
key = int(input("Enter element to search: "))

if search(root, key):
    print("Element found")
else:
    print("Element not found")
