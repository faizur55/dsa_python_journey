# 📓 Week 5 Daily Log

## Day 1 — Binary Tree + DFS
**Date:** 31 March 2026
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

## Day 2 — BFS + Level Order
**Date:** 1 April 2026
**Time:** 3 + hours

### Topics
- BFS vs DFS — wide vs deep
- Queue for BFS — FIFO natural fit
- Level order — freeze size each level
- Minimum depth — BFS stops at first leaf

### Problems
| Problem | Solution |
|---------|----------|
| Level Order Traversal | [code](./solutions/day2_level_order.py) |
| Right Side View | [code](./solutions/day2_right_side_view.py) |
| Minimum Depth | [code](./solutions/day2_min_depth.py) |

### Key Insight
len(queue) at start of each level
= exact nodes in that level.
Freeze it before the for loop!

BFS superpower:
first leaf found = minimum depth ✅
DFS must visit ALL nodes ❌

### Reflection
[your honest thoughts]
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
