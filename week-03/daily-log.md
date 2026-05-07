# 📓 Week 3 Daily Log

## Day 1 — Stacks & Queues
**Date:** 15 March 2026
**Time:** 2 hours

### Topics
- Stack — LIFO, push, pop O(1)
- Queue — FIFO, enqueue, dequeue O(1)
- Why deque not list for queue
- Two stacks = one queue trick

### Problems
| Problem | Solution |
|---------|----------|
| Valid Parentheses | [code](./solutions/day1_valid_parentheses.py) |
| Queue Using Stacks | [code](./solutions/day1_queue_using_stacks.py) |

### Key Insight
Stack = plates. Last in first out.
Queue = ticket counter. First in first out.
Two stacks together = one queue
because double reversal = original order.

### Reflection
[what was easy, what was hard]

---

## Day 2 — Monotonic Stack
**Date:** 16 March 2026
**Time:** 3 Hours

### Topics
- Monotonic decreasing stack
- Next greater element pattern
- Why we store indices not values

### Problems
| Problem | Solution |
|---------|----------|
| Daily Temperatures | [code](./solutions/day2_daily_temperatures.py) |
| Next Greater Element I | [code](./solutions/day2_next_greater_element.py) |

### Key Insight
Stack = waiting room for days without warmer temp.
When warmer day arrives → pop waiting days.
result[popped] = current_index - popped_index.
Each element pushed and popped exactly once → O(n).

### Reflection
[what was easy, what was hard]

---
## Day 3 — Hash Maps Deeper
**Date:** 17 March 2026
**Time:** 2 hours

### Topics
- Frequency + Condition pattern
- Complement lookup extended
- Set for O(n) sequence problems
- Boyer-Moore Voting algorithm

### Problems
| Problem | Solution |
|---------|----------|
| Four Sum II | [code](./solutions/day3_four_sum_ii.py) |
| Majority Element | [code](./solutions/day3_majority_element.py) |
| Longest Consecutive | [code](./solutions/day3_longest_consecutive.py) |

### Key Insight
Every hash map problem asks one of:
  "Have I seen this?"      → set
  "How many times?"        → Counter
  "What's the complement?" → dict lookup
  
Boyer-Moore: majority element survives
all cancellations → O(1) space!

### Reflection
[your honest thoughts]
---

## Day 4 — Advanced String Problems
**Date:** 18 March 2026
**Time:** 3 hours

### Topics
- Min Stack — two stacks in sync
- Decode String — stack saves/restores state
- Find Anagrams — Counter + sliding window

### Problems
| Problem | Solution |
|---------|----------|
| Min Stack | [code](./solutions/day4_min_stack.py) |
| Decode String | [code](./solutions/day4_decode_string.py) |
| Find All Anagrams | [code](./solutions/day4_find_anagrams.py) |

### Key Insight
Min Stack: two stacks stay in sync.
mins[-1] always = current minimum → O(1).

Decode String: stack = memory.
'[' saves state. ']' restores + repeats.

Find Anagrams: Counter + fixed window.
Slide → add right, remove left,
compare counters each step.

### Reflection
[your honest thoughts]
---

## Day 5 — Challenge Day [upcoming]

---

## Day 6 — Review [upcoming]

---

## Day 7 — Publish
- [ ] GitHub pushed
- [ ] Twitter thread posted
- [ ] Blog post published
