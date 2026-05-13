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

## Day 5 — Challenge Day
**Date:** 19 March 2026
**Time:** 5 hours

### Problems
| Problem | Solved Alone? | Solution |
|---------|---------------|----------|
| Asteroid Collision | ✅ Yes | [code](./solutions/day5_asteroid_collision.py) |
| Top K Frequent Words | ✅ Yes | [code](./solutions/day5_top_k_frequent_words.py) |
| Largest Rectangle | 🤝 Together | [code](./solutions/day5_largest_rectangle.py) |

### Key Insight
Stack = waiting room for right-moving asteroids.
Negative asteroid fights anyone waiting.

Sort by tuple (-freq, word) →
frequency DESC + alphabet ASC in one sort.

Monotonic increasing stack →
when bar popped → found right boundary
width = right - left - 1
area = height × width

### Biggest Lesson Today
Paper trace FIRST. Code SECOND.
Never Google before attempting.
Struggle = learning happening. 💪

### Reflection
[your honest thoughts]
---

## Day 6 — Review Day
**Date:** 20 March 2026
**Time:** 2.5+hours

### Weak Spots Drilled
- Monotonic stack — why store indices
- Stack state saving — decode string
- Collision conditions — asteroid

### Problems
| Problem | Solution |
|---------|----------|
| Make The String Great | [code](./solutions/day6_make_string_great.py) |

### Key Insight
Store INDICES not values in monotonic stack
because answer needs POSITION + VALUE.
heights[index] = value ✅
index = position ✅

### Mental Framework
Built complete framework — 8 layers:
  → 3 questions
  → 7 tools
  → 9 patterns
  → complexity cheat sheet
  → 5 step process
  → analogies
  → common mistakes
  → daily drill

---

## Day 7 — Publish
**Date:** 21 March 2026

- [x] GitHub fully updated
- [x] MENTAL_FRAMEWORK.py added to root
- [x] Twitter thread posted
- [x] Blog post published
- [x] Week 3 complete

---

## Day 7 — Publish
- [ ] GitHub pushed
- [ ] Twitter thread posted
- [ ] Blog post published
