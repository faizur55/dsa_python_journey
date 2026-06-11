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

## Day 3 — Top-K Problems [upcoming]

---

## Day 4 — Interval Problems [upcoming]

---

## Day 5 — Challenge Day [upcoming]

---

## Day 6 — Review [upcoming]

---

## Day 7 — Publish + Full Revision [upcoming]
