class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ["+", "-", "*", "/"]
        for element in tokens:
            if element not in operator:
                stack.append(int(element))
            else:
                self.performCalc(element, stack)
        return stack[0]

    def performCalc(self, element, stack):
        a, b = stack.pop(), stack.pop()
        if element == "+":
            stack.append(b+a)
        if element == "-":
            stack.append(b-a)
        if element == "*":
            stack.append(b*a)
        if element == "/":
            stack.append(int(b/a))