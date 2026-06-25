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

## Day 4 — Interval Problems
**Date:** 10 April 2026
**Time:** 5+ hours

### Topics
- Overlap condition: B.start <= A.end
- Insert Interval — 3 phases: before + merge + after
- Non-overlapping — greedy: sort by END, keep earliest
- Meeting Rooms II — min heap tracks room end times

### Problems
| Problem | Solution |
|---------|----------|
| Insert Interval | [code](./solutions/day4_insert_interval.py) |
| Non-overlapping Intervals | [code](./solutions/day4_non_overlapping.py) |
| Meeting Rooms II | [code](./solutions/day4_meeting_rooms.py) |

### Key Insight
Golden Rule:
  Sort by START first — always!
  Exception: non-overlapping → sort by END

Overlap condition:
  B.start <= A.end → overlap
  B.start > A.end  → no overlap

Insert Interval — 3 phases:
  Phase 1: add all before (end < new.start)
  Phase 2: merge all overlapping
  Phase 3: add all remaining

Non-overlapping — greedy:
  Keep earliest ending interval
  Overlap found → remove later ending
  Why? Earlier end = more room for future

Meeting Rooms II — heap:
  Min heap stores room END times
  heap[0] <= start → reuse room
  Else → open new room
  Heap size = answer ✅

### Reflection
[your honest thoughts]
---

## Day 5 — Challenge Day
**Date:** 11 April 2026
**Time:** 6 + Hours

### Problems
| Problem | Solved Alone? | Solution |
|---------|---------------|----------|
| Meeting Rooms | 🤝 Together | [code](./solutions/day5_meeting_rooms.py) |
| Kth Largest Stream | 🤝 Together | [code](./solutions/day5_kth_largest_stream.py) |
| Car Pooling | 🤝 Together | [code](./solutions/day5_car_pooling.py) |

### Key Insights
Meeting Rooms:
  Sort by start → check consecutive overlap
  next.start < current.end → conflict!

Kth Largest Stream:
  Min heap size K always
  heap[0] = Kth largest
  self.k not k — use self everywhere!

Car Pooling:
  Difference array at each stop
  +passengers at start, -passengers at end
  Walk stops → if ever > capacity → False

### Connection
Car Pooling = prefix sum idea from Week 2!
Events at positions → cumulative sum.

### Reflection
[your honest thoughts]

---

## Day 6 — Review [upcoming]

---

## Day 7 — Publish + Full Revision [upcoming]
