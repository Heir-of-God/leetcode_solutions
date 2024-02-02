class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        res: list[int] = []
        l_len: int = len(str(low))
        h_len: int = len(str(high))

        for number_len in range(l_len, h_len + 1, 1):
            start: str = "".join([str(i) for i in range(1, number_len + 1, 1)])
            if low <= int(start) <= high:
                res.append(int(start))

            for l_digit in range(number_len + 1, 10, 1):
                start = start[1:] + str(l_digit)
                if low <= int(start) <= high:
                    res.append(int(start))
                elif int(start) > high:
                    return res
        return res
