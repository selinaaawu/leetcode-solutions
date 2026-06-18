class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # STACK | time: O(nlogn), space: O(n)
        # sort (position, speed) in descending order so closer cars processed first
        # for each car, compute time to reach target, add car time to stack
        # if next car reaches target before/same time, fleet formed, remove from stack

        pair = [(p, s) for p, s in zip(position,speed)]
        pair.sort(reverse = True)

        stack = []
        for p, s in pair:
            time = (target - p) / s
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
        