# 🧠 DSA Mental Framework — Weeks 1-3
# Read once. Drill daily. Own forever.

# ═══════════════════════════════════════
# THE 3 QUESTIONS — Ask for EVERY problem
# ═══════════════════════════════════════
# Q1. What am I STORING?    → TOOL
# Q2. How am I MOVING?      → PATTERN
# Q3. Time + Space cost?    → COMPLEXITY

# ═══════════════════════════════════════
# TOOL SELECTION
# ═══════════════════════════════════════
# "Have I seen this?"          → set
# "What's at this key?"        → dict
# "How many times seen?"       → Counter
# "Group under a key?"         → defaultdict
# "Value at position i?"       → list
# "Remember + reverse order?"  → stack
# "Process in arrival order?"  → deque

# ═══════════════════════════════════════
# PATTERN SELECTION
# ═══════════════════════════════════════
# Sorted array + find pair?         → Two Pointers (L/R)
# Move elements to front/back?      → Two Pointers (slow/fast)
# Three numbers → target?           → Fix one + Two Pointers
# Best subarray, size k given?      → Fixed Sliding Window
# Longest/shortest, condition?      → Variable Sliding Window
# Range sum queries?                → Prefix Sum
# Subarray sum = k?                 → Prefix Sum + dict
# Next greater/smaller?             → Monotonic Stack
# Brackets / state saving?          → Stack

# ═══════════════════════════════════════
# COMPLEXITY CHEAT SHEET
# ═══════════════════════════════════════
# Single loop              → O(n)
# Two nested loops         → O(n²)
# Two separate loops       → O(n)
# Binary search            → O(log n)
# Sort                     → O(n log n)
# Hash map operation       → O(1)
# Stack push/pop           → O(1)
# Prefix array build       → O(n)
# Prefix range query       → O(1)
# Monotonic stack          → O(n)

# ═══════════════════════════════════════
# 5 STEP PROCESS — Every Problem
# ═══════════════════════════════════════
# Step 1 → Read problem TWICE
# Step 2 → Write example on PAPER
# Step 3 → Answer 3 Questions
# Step 4 → TRACE on paper
# Step 5 → THEN open editor
# If stuck → back to Step 2. Never Google first.

# ═══════════════════════════════════════
# ANALOGIES — Lock these in
# ═══════════════════════════════════════
# Stack          → plates (LIFO)
# Queue          → ticket counter (FIFO)
# Set            → bouncer stamp log
# Dict           → phone book
# Counter        → tally chart
# Sliding Window → cardboard frame, array frozen
# Prefix Sum     → car odometer
# Monotonic Stack→ waiting room
# Two Pointers   → two fingers, array frozen

# ═══════════════════════════════════════
# NEVER DO THESE AGAIN
# ═══════════════════════════════════════
# ❌ Pick tool before understanding
# ❌ return inside loop
# ❌ Google before attempting
# ❌ list.pop(0) for queue → use deque
# ❌ s.join(list) → use "".join(list)
# ❌ Store values in monotonic stack
#    → store INDICES (position + value)
# ❌ = for comparison → use ==

# ═══════════════════════════════════════
# DAILY 5-MIN DRILL
# ═══════════════════════════════════════
# Morning → blank paper → write from memory:
#   7 tools + when to use
#   9 patterns + when to use
#   5 step process
# Check → whatever forgot → rewrite 3 times
# 2 weeks of this → automatic forever
