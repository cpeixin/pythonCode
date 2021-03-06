"""
题目：给定一个二叉搜索树(BST)，找到树中第 K 小的节点。
出题人：阿里巴巴出题专家：文景／阿里云 CDN 资深技术专家
参考答案：
* 考察点
基础数据结构的理解和编码能力
递归使用
* 示例
       5
      / \
     3   6
    / \
   2   4
  /
 1

说明：保证输入的 K 满足 1<=K<=(节点数目）

树相关的题目，第一眼就想到递归求解，左右子树分别遍历。联想到二叉搜索树的性质，root 大于左子树，小于右子树。
如果左子树的节点数目等于 K-1，那么 root 就是结果，否则如果左子树节点数目小于 K-1，那么结果必然在右子树，否则就在左子树。
因此在搜索的时候同时返回节点数目，跟 K 做对比，就能得出结果了。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 队栈实现中序遍历
        cnt = 0
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                t = stack.pop()
                cnt += 1
                if cnt == k:
                    return t.val
                root = t.right


if __name__ == '__main__':
    root = [5,3,6,2,4,None,None,1]
    s = Solution
    num = s.kthSmallest(s, root,5)

    print(num)