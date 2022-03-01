# 144. Binary Tree Preorder Traversal
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

"""
Chinese version(中文版本）
本题就是二叉树的前序遍历
给定一二叉树如下图所示：
            1
         /     \
        2       3
      /  \    /   \
     4   5   6    7
其前序遍历为：
1-2-4-5-3-6-7
从树的最左下端开始，每次都按照根节点->左侧叶子节点->右侧叶子结点
根从树的顶端开始
"""

"""
English version
This problem is the preorder traversal of a binary tree.
For a given binary tree:
            1
         /     \
        2       3
      /  \    /  \
     4   5   6    7
It's Preorder traversal:
1-2-4-5-3-6-7
The order is the root -> its left leaf -> the right leaf of the root
(the root starts from the roots at the top of the tree)
"""
"""

python solution

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        stack = [root]

        while stack:
            cur = stack.pop()
            res.append(cur.val)

            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

        return res


# the same code also works in python3(but it seems it run faster)
"""

python3 solution

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = []
        stack = [root]

        while stack:
            cur = stack.pop()
            res.append(cur.val)

            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

        return res

"""
small changes (it runs much slower than the previous solution in python3)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = []
        stack = [root]

        while len(stack) != 0:
            cur = stack.pop()
            res.append(cur.val)

            if cur.right != None:
                stack.append(cur.right)
            if cur.left != None:
                stack.append(cur.left)

        return res

"""
also I add several output, so it will be easier to find how the code works
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = []
        stack = [root]

        while len(stack) != 0:
            cur = stack.pop()
            print("---current---")
            print(cur)
            print(cur.val)
            res.append(cur.val)

            if cur.right != None:
                print("---right---")
                print(cur.right)
                print(cur.right.val)
                stack.append(cur.right)
            if cur.left != None:
                print("---left---")
                print(cur.left)
                print(cur.left.val)
                stack.append(cur.left)

        return res

"""
input:
[1,2,3,4,5,6,7]
output:
---current---
TreeNode{val: 1, left: TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, right: TreeNode{val: 5, left: None, right: None}}, right: TreeNode{val: 3, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}
1
---right---
TreeNode{val: 3, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}
3
---left---
TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, right: TreeNode{val: 5, left: None, right: None}}
2
---current---
TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, right: TreeNode{val: 5, left: None, right: None}}
2
---right---
TreeNode{val: 5, left: None, right: None}
5
---left---
TreeNode{val: 4, left: None, right: None}
4
---current---
TreeNode{val: 4, left: None, right: None}
4
---current---
TreeNode{val: 5, left: None, right: None}
5
---current---
TreeNode{val: 3, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}
3
---right---
TreeNode{val: 7, left: None, right: None}
7
---left---
TreeNode{val: 6, left: None, right: None}
6
---current---
TreeNode{val: 6, left: None, right: None}
6
---current---
TreeNode{val: 7, left: None, right: None}
7

"""