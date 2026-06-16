# 📓 Week 6 Daily Log

## Day 1 — Sorting Algorithms
**Date:** 7 April 2026
**Time:** 3 hours

### Topics
- Merge Sort — split + merge O(n log n)
- Quick Sort — partition O(n log n) avg
- Dutch National Flag — three pointers
- Merge Intervals — sort + overlap check

### Problems
| Problem | Solution |
|---------|----------|
| Sort an Array | [code](./solutions/day1_sort_array.py) |
| Sort Colors | [code](./solutions/day1_sort_colors.py) |
| Merge Intervals | [code](./solutions/day1_merge_intervals.py) |

### Key Insight
Merge Sort:
  split → sort each half → merge
  guaranteed O(n log n) always

Sort Colors:
  three pointers — low, mid, high
  0 → swap with low
  1 → just move mid
  2 → swap with high

Merge Intervals:
  sort by start first!
  overlap = current start <= previous end
  merge = extend previous end

### Reflection
[your honest thoughts]

---

## Day 2 — Heap & Priority Queue
**Date:** 8 April 2026
**Time:** 3+ hours

### Topics
- Min heap vs max heap
- heapq in Python — push, pop, heapify
- Max heap → negate values
- Top-K pattern — min heap size K
- Task scheduler — frequency formula

### Problems
| Problem | Solution |
|---------|----------|
| Kth Largest Element | [code](./solutions/day2_kth_largest.py) |
| K Closest Points | [code](./solutions/day2_k_closest_points.py) |
| Task Scheduler | [code](./solutions/day2_task_scheduler.py) |

### Key Insight
Heap = hospital emergency room
Most important always at top.

Top-K largest → min heap size K:
  Remove smallest when heap > K
  heap[0] = Kth largest ✅

K Closest → no sqrt needed!
  x² + y² enough for comparison

Task Scheduler:
  result = (max_freq-1) * (n+1) + max_count
  always take max with len(tasks)

### Reflection
[your honest thoughts]
---

## Day 3 — Top-K Problems 
## Day 3 — Top-K Deeper + Median
**Date:** 9 April 2026
**Time:** 4 + hours

### Topics
- Two heap pattern — median stream
- Max heap lower half + min heap upper half
- Monotonic deque — sliding window max
- IPO — two heaps working together

### Problems
| Problem | Solution |
|---------|----------|
| Find Median From Stream | [code](./solutions/day3_find_median.py) |
| Sliding Window Maximum | [code](./solutions/day3_sliding_window_max.py) |
| IPO | [code](./solutions/day3_ipo.py) |

### Key Insight
Two Heap Pattern:
  Max heap → lower half (negate values)
  Min heap → upper half
  Balance sizes → median O(1)

Sliding Window Max:
  Monotonic deque stores indices
  Front = current window maximum
  O(n) — each element in/out once

IPO:
  Min heap unlocks affordable projects
  Max heap picks most profitable
  Two heaps working together ✅

### Connection To Previous Weeks
Monotonic deque = Week 3 stack idea
applied to sliding window!
Tools + Patterns combining. 🔥

### Reflection
[your honest thoughts]

---

## Day 4 — Interval Problems [upcoming]

---

## Day 5 — Challenge Day [upcoming]

---

## Day 6 — Review [upcoming]

---

## Day 7 — Publish + Full Revision [upcoming]
