class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set({'+', '-', '*', '/'})
        stack = []
        for c in tokens:
            if c not in operators:
                stack.append(int(c))
                
            elif len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                
                
                
                
                if c == '+':
                    fresult = b + a
                elif c == '-':
                    fresult = b - a
                elif c == '*':
                    fresult = b * a
                elif c == '/':
                    fresult = int(b / a)
                    
                    
                    
                
                stack.append(fresult)

        return stack[0]