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

## Day 3 — Binary Search Tree
**Date:** 2 April 2026
**Time:** 3 hours

### Topics
- BST property — left < node < right
- Search + Insert — O(log n)
- Inorder = sorted order
- Validate with min/max boundaries
- LCA — split point = ancestor

### Problems
| Problem | Solution |
|---------|----------|
| Validate BST | [code](./solutions/day3_validate_bst.py) |
| Lowest Common Ancestor | [code](./solutions/day3_lowest_common_ancestor.py) |
| Kth Smallest | [code](./solutions/day3_kth_smallest.py) |

### Key Insight
Validate BST:
  Can't just check direct children.
  Pass min/max boundaries down recursion.
  Every node must satisfy BOTH boundaries.

LCA in BST:
  Both left → go left
  Both right → go right
  Split → current IS the LCA

Kth Smallest:
  Inorder = sorted → return kth element
  Iterative inorder with stack → O(h) space

### Reflection
[your honest thoughts]

---

## Day 4 — Binary Search [upcoming]

---

## Day 5 — Challenge Day [upcoming]

---

## Day 6 — Review [upcoming]

---

## Day 7 — Publish [upcoming]
