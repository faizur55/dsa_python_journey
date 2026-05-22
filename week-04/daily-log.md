# 📓 Week 4 Daily Log

## Day 1 — Linked List Structure & Traversal
**Date:** 23 March 2026
**Time:** 3 hours

### Topics
- Node structure — val + next pointer
- Traversal — while current loop
- Three pointer reverse — prev, curr, next
- Dummy node pattern — stable starting point

### Problems
| Problem | Solution |
|---------|----------|
| Reverse Linked List | [code](./solutions/day1_reverse_linked_list.py) |
| Merge Two Sorted Lists | [code](./solutions/day1_merge_sorted_lists.py) |

### Key Insight
Arrays → index access O(1)
Linked Lists → traverse from head O(n)

Three pointer reverse:
  save next → reverse pointer → move both

Dummy node → never lose the head.
Return dummy.next at the end.

### Reflection
[your honest thoughts]

---

## Day 2 — Linked List Patterns
**Date:** 24 March 2026
**Time:** 

### Topics
- Slow/Fast pointers — tortoise and hare
- Gap technique — n steps ahead
- Dummy node — edge case handler

### Problems
| Problem | Solution |
|---------|----------|
| Linked List Cycle | [code](./solutions/day2_linked_list_cycle.py) |
| Middle of Linked List | [code](./solutions/day2_middle_linked_list.py) |
| Remove Nth From End | [code](./solutions/day2_remove_nth_from_end.py) |

### Key Insight
Slow/Fast: fast moves 2x → when fast ends
slow is at middle. O(1) space!

Gap technique: move fast n ahead →
move both → slow lands n from end.

Dummy node: never lose head reference.
Always return dummy.next.

### Reflection
[your honest thoughts]

---
## Day 3 — Recursion
**Date:** 25 March 2026
**Time:** 3 hours

### Topics
- Base case + recursive case
- Call stack — hidden O(n) space cost
- Recursion tree — draw before coding
- Iterative vs recursive trade-offs

### Problems
| Problem | Solution |
|---------|----------|
| Reverse List (recursive) | [code](./solutions/day3_reverse_list_recursive.py) |
| Merge Lists (recursive) | [code](./solutions/day3_merge_lists_recursive.py) |
| Flatten Multilevel List | [code](./solutions/day3_flatten_multilevel.py) |

### Key Insight
Every recursive function needs:
  1. BASE CASE    → when to stop
  2. RECURSIVE CASE → smaller problem

Iterative → O(1) space
Recursive → O(n) space (call stack)
Same time. Different space cost.

Always draw recursion tree first!

### Reflection
[your honest thoughts]
---

## Day 4 — Slow/Fast Pointers Deeper
**Date:** 26 March 2026
**Time:** 3 hours

### Topics
- Floyd's algorithm — Phase 1 + Phase 2
- Find cycle start mathematically
- Palindrome — find middle + reverse + compare
- Reorder — find middle + reverse + merge

### Problems
| Problem | Solution |
|---------|----------|
| Linked List Cycle II | [code](./solutions/day4_cycle_detection_ii.py) |
| Palindrome Linked List | [code](./solutions/day4_palindrome_linked_list.py) |
| Reorder List | [code](./solutions/day4_reorder_list.py) |

### Key Insight
3 steps appear in ALL linked list problems:
  Step 1 → find middle (slow/fast)
  Step 2 → reverse second half
  Step 3 → compare OR merge

Step 2 — reverse:
  SAVE → REVERSE → MOVE prev → MOVE current

Step 3 — merge alternately:
  SAVE both nexts → CONNECT → MOVE both

### Reflection
[your honest thoughts]

---

## Day 5 — Challenge Day
**Date:** 27 March 2026
**Time:** 4+ Hours

### Problems
| Problem | Solved Alone? | Solution |
|---------|---------------|----------|
| Add Two Numbers | ✅ Yes | [code](./solutions/day5_add_two_numbers.py) |
| Copy List Random Pointer | ✅ Yes | [code](./solutions/day5_copy_random_list.py) |
| LRU Cache | 🤝 Together | [code](./solutions/day5_lru_cache.py) |

### Key Insights
Add Two Numbers:
  dummy node + carry handles all cases
  while l1 or l2 or carry → never miss carry

Copy Random List:
  two pass → create all nodes first
  then connect next and random
  old_to_new dict maps old → new nodes

LRU Cache:
  dict → O(1) lookup
  doubly linked list → O(1) order tracking
  HEAD side = most recent
  TAIL side = least recent
  evict tail.prev when over capacity

### Biggest Lesson
Design problems = combine two structures.
Ask: "what do I need O(1) for?"
Then pick the right tool for each need.

### Reflection
[your honest thoughts]

---

## Day 6 — Review [upcoming]

---

## Day 7 — Publish [upcoming]
