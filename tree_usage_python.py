# You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:
#
# 1. Create a root node whose value is the maximum value in nums.
# 2. Recursively build the left subtree on the subarray prefix to the left of the maximum value.
# 3. Recursively build the right subtree on the subarray suffix to the right of the maximum value.
# Return the maximum binary tree built from nums.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, nums: List[int]):
        max_ele = 0
        max_i = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > max_ele:
                max_ele = nums[i]
                max_i = i

        ans = TreeNode(nums[max_i])
        if max_i > 0:
            ans.left = self.dfs(nums[:max_i])
        if max_i < n-1:
            ans.right = self.dfs(nums[max_i+1:])

        return ans

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        return self.dfs(nums)

