# 94. Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.


"""
Chinese version(中文版本）
本题就是二叉树的中序遍历
给定一二叉树如下图所示：
            1
         /     \
        2       3
      /  \    /   \
     4   5   6    7
其中序遍历为：
4-2-5-1-6-3-7
从树的最左下端开始，每次都按照左下位置的叶子节点->该叶子的根节点->该根节点的右叶子
"""

"""
English version
This problem is the inorder traversal of a binary tree.
For a given binary tree:

            1
         /     \
        2       3
      /  \    /  \
     4   5   6    7
It's inorder traversal:
4-2-5-1-6-3-7
The order is the left leaf -> its root -> the right leaf of the root
"""

"""
solution in python
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        cur = root
        # res is the results we need to return (the list stores all nodes)
        # stack is a list, but it is used as a stack
        # cur is the current point (where we are in the Binary tree)
        # ↓ if where the pointer points has value or we left some points in the stack
        while cur != None or len(stack) > 0:
            if cur != None:
                stack.append(cur)
                cur = cur.left
                # 如果当前位置不为空，先压栈，向下走，直到走到最左下端
                # if the node is not NONE, we keep the node in the stack, and keep going to its left leaf
            # 请注意这里cur储存的是树
            # please pay attention, cur here stores information about tree
            else:
                cur = stack.pop()
                """ 
                if we add :
                print(cur)
                and the input is [1,2,3]
                it will output:
TreeNode{val: 2, left: None, right: None}
TreeNode{val: 1, left: TreeNode{val: 2, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}
TreeNode{val: 3, left: None, right: None}
                if we add:
                print(cur.val)
                it will out put:
                2
                1
                3
                """
                res.append(cur.val)
                cur = cur.right
                # 如果我们已经走到尽头，就开始判断
                # if cannot go deeper, judge
        return res


"""
it can also be used in python3
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur != None or len(stack) > 0:
            if cur != None:
                stack.append(cur)
                cur = cur.left

            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right

        return res