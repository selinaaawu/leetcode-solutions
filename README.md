# LeetCode Practice

This repository tracks my LeetCode solutions and notes for technical interview preparation.

## Goals

- Practice consistently throughout June
- Strengthen data structures and algorithms fundamentals
- Identify common problem-solving patterns
- Review mistakes and improve speed

## Progress Tracker

| Topic | Solved | Notes |
|---|---:|---|
| Arrays & Hashing | 0 | |
| Two Pointers | 0 | |
| Sliding Window | 0 | |
| Stack | 0 | |
| Binary Search | 0 | |
| Linked List | 0 | |
| Trees | 0 | |
| Heap / Priority Queue | 0 | |
| Backtracking | 0 | |
| Graphs | 0 | |
| Dynamic Programming | 0 | |
| Greedy | 0 | |
| Intervals | 0 | |
| Math & Geometry | 0 | |
| Bit Manipulation | 0 | |

---

## Arrays & Hashing

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| 0217 | Contains Duplicate | Easy | [Python](0217-contains-duplicate/0217-contains-duplicate.py) | hash set: compare length of original array w length of hash set array |
| 0242 | Valid Anagram | Easy | [Python](0242-valid-anagram/0242-valid-anagram.py) | hash map: map letter to occurence, check for equality
| 0001 | Two Sum | Easy | [Python](0001-two-sum/0001-two-sum.py) | hash map: map num to index, check if difference needed is in map
| 0049 | Group Anagrams | Medium | [Python](0049-group-anagrams/0049-group-anagrams.py) | hash map: {character frequency tuple : matching string}, return  values ONLY
| 0347 | Top K Frequent Elements | Medium | [Python](0347-top-k-frequent-elements/0347-top-k-frequent-elements.py) | bucket sort! (1) frequency map {num : frequency}, (2) freq[i] = nums that appear i times, (3) add num to result from largest frequency until k numbers
| 0271 | Encode and Decode Strings | Medium | Python | encode string in format 'length#string', decode string by finding length until # and storing string
| 0238 | Products of Array Except Self | Medium | [Python](0238-product-of-array-except-self.py) | two pass: (1) fill result w prefix product, (2) update result w postfix product
| 0036 | Valid Sudoku | Medium | [Python](0036-valid-sudoku/0036-valid-sudoku.py) | add # to row/col/square seen set, return true if no duplicates
| 0128 | Longest Consecutive Sequence | Medium | [Python](0128-longest-consecutive-sequence/0128-longest-consecutive-sequence.py) | hash set: start counting lcs ONLY if # is beginning of sequence, continue and check if consecutive # exists in set

---

## Two Pointers

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| 125 | Valid Palindrome | Easy | [Python](submissions/0125-valid-palindrome.py) | Skip non-alphanumeric chars, compare left/right |

---

## Sliding Window

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| 121 | Best Time to Buy and Sell Stock | Easy | [Python](submissions/0121-best-time-to-buy-and-sell-stock.py) | Keep track of lowest price so far |

---

## Stack

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| 20 | Valid Parentheses | Easy | [Python](submissions/0020-valid-parentheses.py) | Push opening brackets, match closing brackets |

---

## Binary Search

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|

---

## Linked List

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|

---

## Trees

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|

---

## Heap / Priority Queue

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|

---

## Backtracking

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|

---

## Graphs

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|

---

## Dynamic Programming

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|

---

## Greedy

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|

---

## Intervals

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|

---

## Math & Geometry

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|

---

## Bit Manipulation

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
