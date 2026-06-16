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
| Two Pointers | 0 | 5 | |
| Stack | 0 | 6 | |
| Binary Search | 0 | 7 | |
| Sliding Window | 0 | 6 | |
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
| 0217 | Contains Duplicate | Easy | [Python](0217-contains-duplicate/0217-contains-duplicate.py) | hash set: compare length of original array w length of hash set array |
| 0242 | Valid Anagram | Easy | [Python](0242-valid-anagram/0242-valid-anagram.py) | hash map: map letter to occurence, check for equality | 
| 0001 | Two Sum | Easy | [Python](0001-two-sum/0001-two-sum.py) | hash map: map num to index, check if difference needed is in map | 
| 0049 | Group Anagrams | Medium | [Python](0049-group-anagrams/0049-group-anagrams.py) | hash map: {character frequency tuple : matching string}, return  values ONLY |
| 0347 | Top K Frequent Elements | Medium | [Python](0347-top-k-frequent-elements/0347-top-k-frequent-elements.py) | bucket sort: frequency map {num : frequency}, freq[i] = nums that appear i times, add num to result from largest frequency until k numbers |
| 0271 | Encode and Decode Strings | Medium | Python | encode string in format 'length#string', decode string by finding length until # and storing string |
| 0238 | Products of Array Except Self | Medium | [Python](0238-product-of-array-except-self.py) | two pass: (1) fill result w prefix product, (2) update result w postfix product |
| 0036 | Valid Sudoku | Medium | [Python](0036-valid-sudoku/0036-valid-sudoku.py) | hash set: add # to row/col/square seen set, return true if no duplicates | 
| 0128 | Longest Consecutive Sequence | Medium | [Python](0128-longest-consecutive-sequence/0128-longest-consecutive-sequence.py) | hash set: start counting lcs ONLY if # is beginning of sequence, continue and check if consecutive # exists in set |

---

## Two Pointers

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| 0125 | Valid Palindrome | Easy | [Python](0125-valid-palindrome/0125-valid-palindrome.py) | two pointers: opposite ends, skip non-alphanumeric chars, compare lowercase left/right letters |
| 0167 | Two Sum II Input Array Is Sorted | Medium | [Python](0167-two-sum-ii-input-array-is-sorted/0167-two-sum-ii-input-array-is-sorted.py) | two pointers: opposite ends, if sum too big -> decrement right, if sum too small -> increment left, return for 1-indexed array | 
| 0015 | 3Sum | Medium | [Python](0015-3sum/0015-3sum.py) | fix one number, two pointers on opposite ends to search for remaining two, skip duplicates, if sum too big -> decrement right, if sum too small -> increment left | 
| 0011 | Container With Most Water | Medium | [Python](0011-container-with-most-water/0011-container-with-most-water.py) | two pointers: opposite ends, move pointer from smaller bar to maximize area | 
| 0042 | Trapping Rain Water | Hard | [Python](0042-trapping-rain-water/0042-trapping-rain-water.py) | two pointers: opposite ends, move pointer from shorter wall, update if higher wall, calculate water trapped for each wall | 

---

## Stack

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| 20 | Valid Parentheses | Easy | [Python](submissions/0020-valid-parentheses.py) | Push opening brackets, match closing brackets |
| xxxx | Min Stack | Medium | [Python]() | NOTES | 
| xxxx | Evaluate Reverse Polish Notation | Medium | [Python]() | NOTES | 
| xxxx | Dailly Temperatures | Medium | [Python]() | NOTES | 
| xxxx | Car Fleet | Medium | [Python]() | NOTES | 
| xxxx | Largest Rectangle in Histogram | Hard | [Python]() | NOTES | 

---

## Binary Search

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | Binary Search | Easy | [Python]() | NOTES | 
| xxxx | Search a 2D Matrix | Medium | [Python]() | NOTES | 
| xxxx | Koko Eating Bananas | Medium | [Python]() | NOTES | 
| xxxx | Find Minimum in Rotated Sorted Array | Medium | [Python]() | NOTES | 
| xxxx | Search in Rotated Sorted Array | Medium | [Python]() | NOTES | 
| xxxx | Time Based Key Value Store | Medium | [Python]() | NOTES | 
| xxxx | Median of Two Sorted Arrays | Hard | [Python]() | NOTES | 

---

## Sliding Window

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| 121 | Best Time to Buy and Sell Stock | Easy | [Python](submissions/0121-best-time-to-buy-and-sell-stock.py) | Keep track of lowest price so far |
| xxxx | Longest Substring Without Repeating Characters | Medium | [Python]() | NOTES | 
| xxxx | Longest Repeating Character Replacement | Medium | [Python]() | NOTES | 
| xxxx | Permutation in String | Medium | [Python]() | NOTES | 
| xxxx | Minimum Window Substring | Hard | [Python]() | NOTES | 
| xxxx | Sliding Window Maximum | Hard | [Python]() | NOTES | 

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
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 

---

## Greedy

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 

---

## Graphs

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 

---

## Advanced Graphs

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 

---

## 1-D Dynamic Programming

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 

---

## 2-D Dynamic Programming

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES |

---

## Bit Manipulation

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 

---

## Math & Geometry

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
| xxxx | xxx | DIFFICULTY | [Python]() | NOTES | 
