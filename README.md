# LeetCode Practice

This repository tracks my LeetCode solutions and notes for technical interview preparation.

## Goals

- Practice consistently throughout June
- Strengthen data structures and algorithms fundamentals
- Identify common problem-solving patterns
- Review mistakes and improve speed

## Progress Tracker

| Topic | Solved | Total | Notes |
|---|---:|---:|---|
| Arrays & Hashing | 9 | 9 | |
| Two Pointers | 5 | 5 | |
| Stack | 6 | 6 | |
| Binary Search | 6 | 7 | |
| Sliding Window | 6 | 6 | |
| Linked List | 0 | 11 | |
| Trees | 0 | 15 | |
| Tries | 0 | 3 | |
| Heap / Priority Queue | 0 | 7 | |
| Backtracking | 0 | 10 | |
| Intervals | 0 | 6 | |
| Greedy | 0 | 8 | |
| Graphs | 0  | 13| |
| Advanced Graphs | 0 | 6 | |
| 1-D Dynamic Programming | 0 | 12 | |
| 2-D Dynamic Programming | 0 | 11 | |
| Bit Manipulation | 0 | 7 | |
| Math & Geometry | 0 | 8 | |

---

## Arrays & Hashing

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| 0217 | Contains Duplicate | Easy | [Python](01-arrays-and-hashing/0217-contains-duplicate/0217-contains-duplicate.py) | hash set: compare length of original array w length of hash set array |
| 0242 | Valid Anagram | Easy | [Python](01-arrays-and-hashing/0242-valid-anagram/0242-valid-anagram.py) | hash map: map letter to occurence, check for equality | 
| 0001 | Two Sum | Easy | [Python](01-arrays-and-hashing/0001-two-sum/0001-two-sum.py) | hash map: map num to index, check if difference needed is in map | 
| 0049 | Group Anagrams | Medium | [Python](01-arrays-and-hashing/0049-group-anagrams/0049-group-anagrams.py) | hash map: {character frequency tuple : matching string}, return  values ONLY |
| 0347 | Top K Frequent Elements | Medium | [Python](01-arrays-and-hashing/0347-top-k-frequent-elements/0347-top-k-frequent-elements.py) | bucket sort: frequency map {num : frequency}, freq[i] = nums that appear i times, add num to result from largest frequency until k numbers |
| 0271 | Encode and Decode Strings | Medium | Python | encode string in format 'length#string', decode string by finding length until # and storing string |
| 0238 | Products of Array Except Self | Medium | [Python](01-arrays-and-hashing/0238-product-of-array-except-self.py) | two pass: (1) fill result w prefix product, (2) update result w postfix product |
| 0036 | Valid Sudoku | Medium | [Python](01-arrays-and-hashing/0036-valid-sudoku/0036-valid-sudoku.py) | hash set: add # to row/col/square seen set, return true if no duplicates | 
| 0128 | Longest Consecutive Sequence | Medium | [Python](01-arrays-and-hashing/0128-longest-consecutive-sequence/0128-longest-consecutive-sequence.py) | hash set: start counting lcs ONLY if # is beginning of sequence, continue and check if consecutive # exists in set |

---

## Two Pointers

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| 0125 | Valid Palindrome | Easy | [Python](02-two-pointers/0125-valid-palindrome/0125-valid-palindrome.py) | two pointers: opposite ends, skip non-alphanumeric chars, compare lowercase left/right letters |
| 0167 | Two Sum II Input Array Is Sorted | Medium | [Python](02-two-pointers/0167-two-sum-ii-input-array-is-sorted/0167-two-sum-ii-input-array-is-sorted.py) | two pointers: opposite ends, if sum too big -> decrement right, if sum too small -> increment left, return for 1-indexed array | 
| 0015 | 3Sum | Medium | [Python](02-two-pointers/0015-3sum/0015-3sum.py) | fix one number, two pointers on opposite ends to search for remaining two, skip duplicates, if sum too big -> decrement right, if sum too small -> increment left | 
| 0011 | Container With Most Water | Medium | [Python](02-two-pointers/0011-container-with-most-water/0011-container-with-most-water.py) | two pointers: opposite ends, move pointer from smaller bar to maximize area | 
| 0042 | Trapping Rain Water | Hard | [Python](02-two-pointers/0042-trapping-rain-water/0042-trapping-rain-water.py) | two pointers: opposite ends, move pointer from shorter wall, update if higher wall, calculate water trapped for each wall | 

---

## Stack

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| 0020 | Valid Parentheses | Easy | [Python](03-stack/0020-valid-parentheses/0020-valid-parentheses.py) | stack: push opening bracket, pop matching closing bracket or invalid string |
| 0155 | Min Stack | Medium | [Python](03-stack/0155-min-stack/0155-min-stack.py) | two stack, minStack stores min value UP TO value in stack | 
| 0159 | Evaluate Reverse Polish Notation | Medium | [Python](03-stack/0150-evaluate-reverse-polish-notation/0150-evaluate-reverse-polish-notation.py) | stack: push num onto stack, if operator -> pop two #s, apply operation, push result onto stack | 
| 0739 | Dailly Temperatures | Medium | [Python](03-stack/0739-daily-temperatures/0739-daily-temperatures.py) | stack: store (index, temp), if curr temp > stack[-1] -> warmer day found, compute difference in days, otherwise add to stack | 
| 0853 | Car Fleet | Medium | [Python](03-stack/0853-car-fleet/0853-car-fleet.py) | sort (position, speed) in descending order, compute time to reach target, if next car reaches target after most recent -> new fleet, add time to stack, otherwise ignore  | 
| 0084 | Largest Rectangle in Histogram | Hard | [Python](03-stack/0084-largest-rectangle-in-histogram/0084-largest-rectangle-in-histogram.py) | stack: store (index, height) in increasing order, if shorter bar -> pop and update max area, otherwise -> push w leftmost index, pop remaining bars and update max area | 

---

## Binary Search

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| 0704 | Binary Search | Easy | [Python](04-binary-search/0704-binary-search/0704-binary-search.py) | exact binary search: [0, len(nums) - 1], l <= r, if num[m] too big, m = r - 1, num[m] too small, m = l + 1|
| 0074 | Search a 2D Matrix | Medium | [Python](04-binary-search/0074-search-a-2d-matrix/0074-search-a-2d-matrix.py) | exact binary search: [0, rows * cols - 1] flatten matrix into sorted array, map mid to matrix w row = m // cols, col = m % cols | 
| 0875 | Koko Eating Bananas | Medium | [Python](04-binary-search/0875-koko-eating-bananas/0875-koko-eating-bananas.py) | binary search answer array: [1, max(piles)], for each rate -> calculate time to eat all piles, if time < h -> eat less, otherwise eat more | 
| 0153 | Find Minimum in Rotated Sorted Array | Medium | [Python](04-binary-search/0153-find-minimum-in-rotated-sorted-array/0153-find-minimum-in-rotated-sorted-array.py) | lower bound binary search: [0, len(nums) - 1], l < r, if nums[mid] < nums[r] -> rotated, check right, otherwise nums[mid] sorted array -> check left
| 0033 | Search in Rotated Sorted Array | Medium | [Python](04-binary-search/0033-search-in-rotated-sorted-array/0033-search-in-rotated-sorted-array.py) | exact binary search: [0, len(nums) - 1, l <= r, for rotated/sorted half, compare target to nums[mid] or nums[r] to determine whether to check left/right | 
| 0981 | Time Based Key Value Store | Medium | [Python](04-binary-search/0981-time-based-key-value-store/0981-time-based-key-value-store.py) | store is dict where key : list of (value, timestamp), find rightmost timestamp <= target: [0, len(store[key]], if m < target -> save, check right, otherwise -> check left | 
| xxxx | Median of Two Sorted Arrays | Hard | [Python](04-binary-search/) | NOTES | 

---

## Sliding Window

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| 0121 | Best Time to Buy and Sell Stock | Easy | [Python](04-sliding-window/0121-best-time-to-buy-and-sell-stock/0121-best-time-to-buy-and-sell-stock.py) | two pointers: expand r, if buy > sell -> buy = sell, otherwise -> update max profit |
| 0003 | Longest Substring Without Repeating Characters | Medium | [Python](04-sliding-window/0003-longest-substring-without-repeating-characters/0003-longest-substring-without-repeating-characters.py) | sliding window/variable: hash map stores {char : index}, expand r, add s[r] to map, update max length, if s[r] in map -> update l = last index + 1 OR l (not backward) | 
| 0424 | Longest Repeating Character Replacement | Medium | [Python](04-sliding-window/0424-longest-repeating-character-replacement/0424-longest-repeating-character-replacement.py) | sliding window/variable: hash map stores {char : count}, expand r, update s[r] count, max frequency, max length, while window size - max frequency > k -> invalid state, update s[l] count and shrink l | 
| 0567 | Permutation in String | Medium | [Python](04-sliding-window/0567-permutation-in-string/0567-permutation-in-string.py) | sliding window/fixed: initialize 26-len character frequency arrays, update total matches of two states, expand r, if matches == 26 -> permutation found, add right character to window state, update matches, remove left character from window state, update matches, update l count to maintain fixed size | 
| 0076 | Minimum Window Substring | Hard | [Python](04-sliding-window/0076-minimum-window-substring/0076-minimum-window-substring.py) | sliding window/varialbe: hash map stores {char : count}, initialize valid state, expand r, add s[r] to window and update matching count as needed, while window has all required characters -> update pointers, shrink l until invalid | 
| 0239 | Sliding Window Maximum | Hard | [Python](04-sliding-window/0239-sliding-window-maximum/0239-sliding-window-maximum.py) | sliding window/fixed: deque stores indices in decreasing order, deque[0] ALWAYS sotres curr max, expand r, remove nums < nums[r], add r to deque, shrink l if window out of range, record max when window size == k | 

---

## Linked List

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | Reverse Linked List | Easy | [Python]() | NOTES | 
| xxxx | Merge Two Sorted Lists  | Easy | [Python]() | NOTES | 
| xxxx | Linked List Cycle | Easy | [Python]() | NOTES | 
| xxxx | Reorder List | Medium | [Python]() | NOTES | 
| xxxx | Remove Nth Node From End of List | Medium | [Python]() | NOTES | 
| xxxx | Copy List With Random Pointer | Medium | [Python]() | NOTES | 
| xxxx | Add Two Numbers | Medium | [Python]() | NOTES | 
| xxxx | Find the Duplicate Number | Medium | [Python]() | NOTES | 
| xxxx | LRU Cache | Medium | [Python]() | NOTES | 
| xxxx | Merge K Sorted Lists | Hard | [Python]() | NOTES | 
| xxxx | Reverse Nodes in K Group | Hard | [Python]() | NOTES | 

---

## Trees

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | Invert Binary Tree | Easy | [Python]() | NOTES | 
| xxxx | Maximum Depth of Binary Tree | Easy | [Python]() | NOTES | 
| xxxx | Diameter of Binary Tree | Easy | [Python]() | NOTES | 
| xxxx | Balanced Binary Tree | Easy | [Python]() | NOTES | 
| xxxx | Same Tree | Easy | [Python]() | NOTES | 
| xxxx | Subtree of Another Tree | Easy | [Python]() | NOTES | 
| xxxx | Lowest Common Ancestor of a Binary Search Tree | Medium | [Python]() | NOTES | 
| xxxx | Binary Tree Level Order Traversal | Medium | [Python]() | NOTES | 
| xxxx | Binary Tree Right Side View | Medium | [Python]() | NOTES | 
| xxxx | Count Good Nodes in Binary Tree | Medium | [Python]() | NOTES | 
| xxxx | Validate Binary Search Tree | Medium | [Python]() | NOTES | 
| xxxx | Kth Smallest Element in a BST | Medium | [Python]() | NOTES | 
| xxxx | Construct Binary Tree From Preorder and Inorder Traversal | Medium | [Python]() | NOTES | 
| xxxx | Binary Tree Maximum Path Sum | Hard | [Python]() | NOTES | 
| xxxx | Serialize and Deserialize Binary Tree | Hard | [Python]() | NOTES | 

---

## Tries

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | Implement Trie Prefix Tree | Medium | [Python]() | NOTES | 
| xxxx | Design Add and Search Words Data Structure | Medium | [Python]() | NOTES | 
| xxxx | Word Search II | Hard | [Python]() | NOTES | 

---

## Heap / Priority Queue

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | Kth Largest Element in a Stream | Easy | [Python]() | NOTES | 
| xxxx | Last Stone Weight | Easy | [Python]() | NOTES | 
| xxxx | K Closest Points to Origin | Medium | [Python]() | NOTES | 
| xxxx | Kth Largest Element in An Array | Medium | [Python]() | NOTES | 
| xxxx | Task Scheduler | Medium | [Python]() | NOTES | 
| xxxx | Design Twitter | Medium | [Python]() | NOTES | 
| xxxx | Find Median From Data Stream | Hard | [Python]() | NOTES | 

---

## Backtracking

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | Subsets | Medium | [Python]() | NOTES | 
| xxxx | Combination Sum | Medium | [Python]() | NOTES | 
| xxxx | Combination Sum II | Medium | [Python]() | NOTES | 
| xxxx | Permutations | Medium | [Python]() | NOTES | 
| xxxx | Subsets II | Medium | [Python]() | NOTES | 
| xxxx | Generate Parentheses | Medium | [Python]() | NOTES | 
| xxxx | Word Search | Medium | [Python]() | NOTES | 
| xxxx | Palindrom Partitioning | Medium | [Python]() | NOTES | 
| xxxx | Letter Combinations of a Phone Number | Medium | [Python]() | NOTES | 
| xxxx | N Queens | Hard | [Python]() | NOTES | 

---

## Intervals

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| Insert Interval | Medium | DIFFICULTY | [Python]() | NOTES | 
| Merge Intervals | Medium | DIFFICULTY | [Python]() | NOTES | 
| Non Overlapping Intervals | Medium | DIFFICULTY | [Python]() | NOTES | 
| Meeting Rooms | Easy | DIFFICULTY | [Python]() | NOTES | 
| Meeting Rooms II | Medium | DIFFICULTY | [Python]() | NOTES | 
| Minimum Interval to Include Each Query | Hard | DIFFICULTY | [Python]() | NOTES | 

---

## Greedy

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | Maximum Subarray | Medium | [Python]() | NOTES | 
| xxxx | Jump Game | Medium | [Python]() | NOTES | 
| xxxx | Jump Game II | Medium | [Python]() | NOTES | 
| xxxx | Gas Station | Medium | [Python]() | NOTES | 
| xxxx | Hand of Straights | Medium | [Python]() | NOTES | 
| xxxx | Merge Triplets to Form Target Triplet | Medium | [Python]() | NOTES | 
| xxxx | Partition Labels | Medium | [Python]() | NOTES | 
| xxxx | Valid Parenthesis String | Medium | [Python]() | NOTES | 

---

## Graphs

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | Number of Islands | Medium | [Python]() | NOTES | 
| xxxx | Max Area of Island | Medium | [Python]() | NOTES | 
| xxxx | Clone Graph | Medium | [Python]() | NOTES | 
| xxxx | Walls and Gates | Medium | [Python]() | NOTES | 
| xxxx | Rotting Oranges | Medium | [Python]() | NOTES | 
| xxxx | Pacific Atlantic Water Flow | Medium | [Python]() | NOTES | 
| xxxx | Surrounded Regions | Medium | [Python]() | NOTES | 
| xxxx | Course Schedule | Medium | [Python]() | NOTES | 
| xxxx | Course Schedule II | Medium | [Python]() | NOTES | 
| xxxx | Graph Valid Tree | Medium | [Python]() | NOTES | 
| xxxx | Number of Connected Components in An Undirected Graph | Medium | [Python]() | NOTES | 
| xxxx | Redundant Connection | Medium | [Python]() | NOTES | 
| xxxx | Word Ladder | Hard | [Python]() | NOTES | 

---

## Advanced Graphs

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | Network Delay Time | Medium | [Python]() | NOTES | 
| xxxx | Reconstruct Itinerary | Hard | [Python]() | NOTES | 
| xxxx | Min Cost to Connect All Points | Medium | [Python]() | NOTES | 
| xxxx | Swim in Rising Water | Hard | [Python]() | NOTES | 
| xxxx | Alien Dictionary | Hard | [Python]() | NOTES | 
| xxxx | Cheapest Flights Within K Stops | Medium | [Python]() | NOTES | 

---

## 1-D Dynamic Programming

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | Climbing Stairs | Easy | [Python]() | NOTES | 
| xxxx | Min Cost Climbing Stairs | Easy | [Python]() | NOTES | 
| xxxx | House Robber | Medium | [Python]() | NOTES | 
| xxxx | House Robber II | Medium | [Python]() | NOTES | 
| xxxx | Longest Palindrome Substring | Medium | [Python]() | NOTES | 
| xxxx | Palindromic Substrings | Medium | [Python]() | NOTES | 
| xxxx | Decode Ways | Medium | [Python]() | NOTES | 
| xxxx | Coin Change | Medium | [Python]() | NOTES | 
| xxxx | Maximum Product Subarray | Medium | [Python]() | NOTES | 
| xxxx | Word Break | Medium | [Python]() | NOTES | 
| xxxx | Longest Increasing Subsequence | Medium | [Python]() | NOTES | 
| xxxx | Partition Equal Subset Sum | Medium | [Python]() | NOTES | 

---

## 2-D Dynamic Programming

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | Unique Paths | Medium | [Python]() | NOTES | 
| xxxx | Longest Common Subsequence | Medium | [Python]() | NOTES | 
| xxxx | Best Time to Buy And Sell Stock With Cooldown | Medium | [Python]() | NOTES | 
| xxxx | Coin Change II | Medium | [Python]() | NOTES | 
| xxxx | Target Sum | Medium | [Python]() | NOTES | 
| xxxx | Interleaving String | Medium | [Python]() | NOTES | 
| xxxx | Longest Increasing Path In a Matrix | Hard | [Python]() | NOTES | 
| xxxx | Distinct Subsequences | Hard | [Python]() | NOTES | 
| xxxx | Edit Distance | Medium | [Python]() | NOTES | 
| xxxx | Burst Balloons | Hard | [Python]() | NOTES |
| xxxx | Regular Experssion Matching | Hard | [Python]() | NOTES |

---

## Bit Manipulation

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | Single Number | Easy | [Python]() | NOTES | 
| xxxx | Number of 1 Bits | Easy | [Python]() | NOTES | 
| xxxx | Counting Bit | Easy | [Python]() | NOTES | 
| xxxx | Reverse Bits | Easy | [Python]() | NOTES | 
| xxxx | Missing Number | Easy | [Python]() | NOTES | 
| xxxx | Sum of Two Integers | Medium | [Python]() | NOTES | 
| xxxx | Reverse Integers | Medium | [Python]() | NOTES | 

---

## Math & Geometry

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | Rotate Image | Medium | [Python]() | NOTES | 
| xxxx | Spiral Matrix | Medium | [Python]() | NOTES | 
| xxxx | Set Matrix Zeroes | Medium | [Python]() | NOTES | 
| xxxx | Happy Number | Easy | [Python]() | NOTES | 
| xxxx | Plus One | Easy | [Python]() | NOTES | 
| xxxx | Pow(x, n) | Medium | [Python]() | NOTES | 
| xxxx | Multiply Strings | Medium | [Python]() | NOTES | 
| xxxx | Detect Squares | Medium | [Python]() | NOTES | 
