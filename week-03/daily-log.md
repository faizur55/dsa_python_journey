# 📓 Week 3 Daily Log

## Day 1 — Stacks & Queues
**Date:** [your date]
**Time:** [hours]

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
**Date:** [your date]
**Time:** [hours]

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

## Day 3 — [upcoming]

---

## Day 4 — [upcoming]

---

## Day 5 — Challenge Day [upcoming]

---

## Day 6 — Review [upcoming]

---

## Day 7 — Publish
- [ ] GitHub pushed
- [ ] Twitter thread posted
- [ ] Blog post published
