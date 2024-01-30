class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        def calculate(n1: int | str, n2: int | str, op: str) -> int | float:
            n1, n2 = int(n1), int(n2)
            if op == "+":
                return n1 + n2
            elif op == "-":
                return n1 - n2
            elif op == "*":
                return n1 * n2
            elif op == "/":
                return int(n1 / n2)
            return 0

        while len(tokens) != 1:
            ind = 0
            while tokens[ind] not in "+-*/":
                ind += 1
            n1, n2, op = [tokens.pop(ind - 2) for _ in range(3)]
            res: int | float = calculate(n1, n2, op)
            tokens.insert(ind - 2, str(res))

        return int(tokens[0])
