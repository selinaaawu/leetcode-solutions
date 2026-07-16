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
| Linked List | 9 | 11 | |
| Trees | 14 | 15 | |
| Tries | 3 | 3 | |
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
| 0121 | Best Time to Buy and Sell Stock | Easy | [Python](05-sliding-window/0121-best-time-to-buy-and-sell-stock/0121-best-time-to-buy-and-sell-stock.py) | two pointers: expand r, if buy > sell -> buy = sell, otherwise -> update max profit |
| 0003 | Longest Substring Without Repeating Characters | Medium | [Python](05-sliding-window/0003-longest-substring-without-repeating-characters/0003-longest-substring-without-repeating-characters.py) | sliding window/variable: hash map stores {char : index}, expand r, add s[r] to map, update max length, if s[r] in map -> update l = last index + 1 OR l (not backward) | 
| 0424 | Longest Repeating Character Replacement | Medium | [Python](05-sliding-window/0424-longest-repeating-character-replacement/0424-longest-repeating-character-replacement.py) | sliding window/variable: hash map stores {char : count}, expand r, update s[r] count, max frequency, max length, while window size - max frequency > k -> invalid state, update s[l] count and shrink l | 
| 0567 | Permutation in String | Medium | [Python](05-sliding-window/0567-permutation-in-string/0567-permutation-in-string.py) | sliding window/fixed: initialize 26-len character frequency arrays, update total matches of two states, expand r, if matches == 26 -> permutation found, add right character to window state, update matches, remove left character from window state, update matches, update l count to maintain fixed size | 
| 0076 | Minimum Window Substring | Hard | [Python](05-sliding-window/0076-minimum-window-substring/0076-minimum-window-substring.py) | sliding window/varialbe: hash map stores {char : count}, initialize valid state, expand r, add s[r] to window and update matching count as needed, while window has all required characters -> update pointers, shrink l until invalid | 
| 0239 | Sliding Window Maximum | Hard | [Python](05-sliding-window/0239-sliding-window-maximum/0239-sliding-window-maximum.py) | sliding window/fixed: deque stores indices in decreasing order, deque[0] ALWAYS sotres curr max, expand r, remove nums < nums[r], add r to deque, shrink l if window out of range, record max when window size == k | 

---

## Linked List

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| 0206 | Reverse Linked List | Easy | [Python](07-linked-list/0206-reverse-linked-list/0206-reverse-linked-list.py) | for each node: store next pointer, update pointer to point backwards, move prev & curr pointer forward, return prev (last element is new head) | 
| 0021 | Merge Two Sorted Lists  | Easy | [Python](07-linked-list/0021-merge-two-sorted-lists/0021-merge-two-sorted-lists.py) | keep pointer to head, while both lists have nodes -> add smaller node to node.next and update list & node, add remaining nodes from non-empty list | 
| 0141 | Linked List Cycle | Easy | [Python](07-linked-list/0141-linked-list-cycle/0141-linked-list-cycle.py) | slow, fast = head, head, slow pointer moves 1, fast pointer moves 2, if cycle -> fast == slow eventually, otherwise fast == null eventually  | 
| 0143 | Reorder List | Medium | [Python](07-linked-list/0143-reorder-list/0143-reorder-list.py) | find middle of linked list using slow/fast, break halves apart, reverse second half of list, merge two halves one-by-one (first then second) | 
| 0019 | Remove Nth Node From End of List | Medium | [Python](07-linked-list/0019-remove-nth-node-from-end-of-list/0019-remove-nth-node-from-end-of-list.py) |  dummy = (0, head) since head can be removed, left, right points to dummy, move right pointer n times, move both pointers until right reaches end, delete node, return dummy.next | 
| 0138 | Copy List With Random Pointer | Medium | [Python](07-linked-list/0138-copy-list-with-random-pointer/0138-copy-list-with-random-pointer.py) | hash map stores deep copy of node, link value, next pointer, random pointer using hash map | 
| 0002 | Add Two Numbers | Medium | [Python](07-linked-list/0002-add-two-numbers/0002-add-two-numbers.py) | keep pointer to head, while either list has more digits or carry exists -> add two digits and carry, update carry, save remainder into next node, update all pointers | 
| 0287 | Find the Duplicate Number | Medium | [Python](07-linked-list/0287-find-the-duplicate-number/0287-find-the-duplicate-number.py) | treat array as linked list where value tells next index, slow, fast = 0, 0, while slow != fast -> find intersection, while start != slow -> find cycle entrance  | 
| 0146 | LRU Cache | Medium | [Python](07-linked-list/0146-lru-cache/0146-lru-cache.py) | hash map & doubly linked list, left/right nodes point to least/most recently used nodes, remove/insert functions for easy removal/insertion, get key -> move node to right, return value, put key -> create/update key-value pair, insert to right, remove leftmost node if at capacity| 
| xxxx | Merge K Sorted Lists | Hard | [Python](07-linked-list/) | NOTES | 
| xxxx | Reverse Nodes in K Group | Hard | [Python](07-linked-list/) | NOTES | 

---

## Trees

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| 0226 | Invert Binary Tree | Easy | [Python](07-trees/0226-invert-binary-tree/0226-invert-binary-tree.py) | base case -> null <br> recursive DFS: swap left/right childiren, call to invert left/right subtree, return root <br> iterative DFS: stack, pop node, swap left/right chilidren, if left/right child exists -> append to stack, return node <br> BFS: queue (deque), popleft (FIFO), swap left/right children, if left/right chid exists -> append to queue, return root | 
| 0104 | Maximum Depth of Binary Tree | Easy | [Python](07-trees/0104-maximum-depth-of-binary-tree/0104-maximum-depth-of-binary-tree.py) | base case -> 0 <br> recrusive DFS: compute left/right depth, return 1 + max(left, right) <br> iterative DFS: stack stores (node, depth), pop stack, update max depth, append left/right children w depht + 1 <br> BFS: queue, count levels traversed until queue empty | 
| 0543 | Diameter of Binary Tree | Easy | [Python](07-trees/0543-diameter-of-binary-tree/0543-diameter-of-binary-tree.py) | diameter = left subtree height + right subtree height <br> recursive DFS: dfs(root) returns height of each node & global diameter, track max diameter seen | 
| 0110 | Balanced Binary Tree | Easy | [Python](07-trees/0110-balanced-binary-tree/0110-balanced-binary-tree.py) | dfs(root) returns (balanced subtree, height), tree balanced IFF left/right subtree balanced AND left subtree height - right subtree height <= 1, return last balanced subtree boolean | 
| 0100 | Same Tree | Easy | [Python](07-trees/0100-same-tree/0100-same-tree.py) | same tree has identical structure & values, if both nodes are equal/null -> return True, if one node null or values differ -> return False | 
| 0572 | Subtree of Another Tree | Easy | [Python](07-trees/0572-subtree-of-another-tree/0572-subtree-of-another-tree.py) | fully compare subtree of root == subroot, if identical -> subtree found, otherwise -> search left/right children, edge cases for root & subroot | 
| 0235 | Lowest Common Ancestor of a Binary Search Tree | Medium | [Python](07-trees/0235-lowest-common-ancestor-of-a-binary-search-tree/0235-lowest-common-ancestor-of-a-binary-search-tree.py) | BST means left subtree < node < right subtree <br> iterative: recruse root tree, if both values < curr -> search left subtree, if both values > curr -> search right subtree, else -> split point aka LCA <br> recurisve: base case: None, same idea as iterative | 
| 0102 | Binary Tree Level Order Traversal | Medium | [Python](07-trees/0102-binary-tree-level-order-traversal/0102-binary-tree-level-order-traversal.py) | BFS, list stores every level & queue stores values, queue = deque([root]), while queue -> current level = [], for len(queue) nodes -> pop nodes from queue, add value to curr level, push left/chlidren to queue | 
| 0199 | Binary Tree Right Side View | Medium | [Python](07-trees/0199-binary-tree-right-side-view/0199-binary-tree-right-side-view.py) | BFS, list stores rightmost node & queue stores values, queue = deque([root]), while queue -> current level = [], for len(queue) nodes -> pop nodes from queue, update rightmost node, push left/chlidren to queue, add rightmost value to list | 
| 1448 | Count Good Nodes in Binary Tree | Medium | [Python](07-trees/1448-count-good-nodes-in-binary-tree/1448-count-good-nodes-in-binary-tree.py) | good node = no earlier nodes has greater value <br> preorder recrusive DFS, dfs(node, max_value), for every node -> if node >= max value -> add by 1, otherwise -> 0, update max value in path, recurse left/right child w updated max_value, return sum of all values | 
| 0098 | Validate Binary Search Tree | Medium | [Python](07-trees/0098-validate-binary-search-tree/0098-validate-binary-search-tree.py) | top down recursive DFS, dfs(node, low, high), valid BST has nodes (low, high), check left subtree w node less than parent, check right subtree w node greater than parent, tighten bounds while recursing tree | 
| 0230 | Kth Smallest Element in a BST | Medium | [Python](07-trees/0230-kth-smallest-element-in-a-bst/0230-kth-smallest-element-in-a-bst.py) | inorder DFS: visit left subtree, check if kth element, update kth value, decrement count, visit right subtree   | 
| 0105 | Construct Binary Tree From Preorder and Inorder Traversal | Medium | [Python](07-trees/0105-construct-binary-tree-from-preorder-and-inorder-traversal/0105-construct-binary-tree-from-preorder-and-inorder-traversal.py) | preorder tells first node, inorder tells left/right subtree <br> top down recursive DFS: time = O(n^2), find position of preorder[0] in inorder, build left/right subtree w new preorder/inorder slicing <br> top down recursive DFS + hashmap: time = O(n), hashmap stores {value, index} for inorder list O(1) time, preIndex tracks next preorder value, dfs(left, right), get root value, create node, look up inorder index, build left/right with inorder index <br> top down recursive DFS: O(n), preIndex = inIndex = 0, dfs(limit), if no more nodes or limit met -> return None, create node, build left/right with updated limit values | 
| xxxx | Binary Tree Maximum Path Sum | Hard | [Python](07-trees/) | NOTES | 
| 0297 | Serialize and Deserialize Binary Tree | Hard | [Python](07-trees/0297-serialize-and-deserialize-binary-tree/0297-serialize-and-deserialize-binary-tree.py) | top down preorder DFS <br> serialize: store preorder traversal in result list, dfs(root) if null -> store "N", if value -> store str(value), return result as string, deserialize: split string to list, index = 0, dfs(), if "N" -> null node, if value -> create node w value, increment index as needed <br> inorder BFS saves level by level <br> serialize: pop leftmost node, if null -> store "N", otherwise -> result append str(value), queue append left/right, return result as string, deserialize: split string to list, create queue w root, index = 1, while queue -> create left/right child & append to queue, increment index as needed | 

---

## Tries

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| 0208 | Implement Trie Prefix Tree | Medium | [Python](08-tries/0208-implement-trie-prefix-tree/0208-implement-trie-prefix-tree.py) | initialize root = TrieNode <br> insert(word): for each character, if not in tree -> create trienode, iterate character by character, mark endOfWord <br> search(word): if char not in tree, word does not exist, return if endOfWord <br> startsWith(word): if char not in tree, prefix does not exist, return if all matching | 
| 0211 | Design Add and Search Words Data Structure | Medium | [Python](08-tries/0211-design-add-and-search-words-data-structure/0211-design-add-and-search-words-data-structure.py) | search(word) uses recursive dfs(j, root) where j = index of word, root = current TrieNode, compare every character, if "." -> iterate EVERY child w dfs(i + 1, child), True if valid else False, if regular character not exist -> False | 
| 0212 | Word Search II | Hard | [Python](08-tries/0212-word-search-ii/0212-word-search-ii.py) | class trienode w index = index of word (mark end) or -1 <br> create trie of all words, for all row/col, dfs() <br> dfs(r, c, node): if out of bounds or board[r][c] already visited or not a trie children -> return, iterate to child, if end of word -> add to result & mark index = -1, mark board[r][c] as visited, dfs() 4 neighbors, restore board[r][c], prune for further optimization (if child trienode has no children -> remove from parent) | 

---

## Heap / Priority Queue

| # | Problem | Difficulty | Solution | Notes |
|---|---|---|---|---|
| xxxx | Kth Largest Element in a Stream | Easy | [Python](09-heap-priority-queue/) | NOTES | 
| xxxx | Last Stone Weight | Easy | [Python](09-heap-priority-queue/) | NOTES | 
| xxxx | K Closest Points to Origin | Medium | [Python](09-heap-priority-queue/) | NOTES | 
| xxxx | Kth Largest Element in An Array | Medium | [Python](09-heap-priority-queue/) | NOTES | 
| xxxx | Task Scheduler | Medium | [Python](09-heap-priority-queue/) | NOTES | 
| xxxx | Design Twitter | Medium | [Python](09-heap-priority-queue/) | NOTES | 
| xxxx | Find Median From Data Stream | Hard | [Python](09-heap-priority-queue/) | NOTES | 

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
