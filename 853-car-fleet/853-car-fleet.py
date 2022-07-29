class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(pos, sped) for pos, sped in zip(position, speed)]
        pair.sort(reverse=True)
        for pos, sped in pair:
            stack.append([pos,sped])
            if len(stack) >= 2 and self.getTime(target,stack[-2][1],stack[-2][0]) >= self.getTime(target,stack[-1][1],stack[-1][0]):
                stack.pop()

        return len(stack)
    def getTime(self,target,speed,pos):
        return (target-pos)/speed