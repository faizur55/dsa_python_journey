# 📓 Week 5 Daily Log

## Day 1 — Binary Tree + DFS
**Date:** 31 March 31 2026
**Time:** 2 hours

### Topics
- TreeNode — val, left, right
- DFS — preorder, inorder, postorder
- Recursive tree template
- Base case: if not node → return

### Problems
| Problem | Solution |
|---------|----------|
| Maximum Depth | [code](./solutions/day1_max_depth.py) |
| Invert Binary Tree | [code](./solutions/day1_invert_tree.py) |
| Same Tree | [code](./solutions/day1_same_tree.py) |

### Key Insight
Tree recursion template:
  if not node: return base_case
  left  = solve(node.left)
  right = solve(node.right)
  return combine(left, right)

Most tree problems fit this template!

### Reflection
[your honest thoughts]

---

## Day 2 — BFS + Level Order [upcoming]

---

## Day 3 — BST [upcoming]

---

## Day 4 — Binary Search [upcoming]

---

## Day 5 — Challenge Day [upcoming]

---

## Day 6 — Review [upcoming]

---

## Day 7 — Publish [upcoming]
