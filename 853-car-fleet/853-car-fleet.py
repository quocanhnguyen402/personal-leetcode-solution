class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(pos, sped) for pos, sped in zip(position, speed)]
        pair.sort(reverse=True)
        for pos, sped in pair:
            stack.append(self.getTime(target,sped,pos))
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)
    def getTime(self,target,speed,pos):
        return (target-pos)/speed