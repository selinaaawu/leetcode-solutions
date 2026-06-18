class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # STACK | time: O(nlogn), space: O(n)
        # sort (position, speed) in descending order so closer cars processed first
        # for each car, compute time to reach target
        # if next car reaches target after most recent, new fleet, add to stack
        # otherwise next car reaches target before/with most recent, fleet formed, ignore

        pair = [(p, s) for p, s in zip(position,speed)]
        pair.sort(reverse = True)

        stack = []
        for p, s in pair:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
        