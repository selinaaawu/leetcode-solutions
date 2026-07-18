class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        ## MAX HEAP | time: O(# tasks), space: O(1)
        # run task with most remaining occurencies bc they are hardest to fit
        # after running task, go to cooldown queue w next time it's available
        # add back to heap after cooldown finished
        # if heap empty, jump time forward to next time task is available

        # count frequency of each task
        freq = Counter(tasks)

        # max heap = remaining count for retrieval of most frequent task
        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)

        # queue (FIFO) = (idle time, -count) for processing tasks
        queue = deque()
        
        time = 0
        while maxHeap or queue:
            # one CPU cycle passed
            time += 1

            # if heap is not empty, pop most frequent task, decrement count
            # push (time + n, remaining count) into cooldown queue
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    queue.append((time + n, count))
            
            # most important for optimization !!!
            # if heap is empty but cooldown queue is not empty
            # update time to next available time in cooldown queue
            if not maxHeap and queue:
                time = queue[0][0]

            # if front of cooldown queue has next available time == curr time, 
            # remove from queue & push remaining count back into heap
            if queue and queue[0][0] == time:
                heapq.heappush(maxHeap, queue.popleft()[1])

        return time
        