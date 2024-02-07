class Solution:
    def frequencySort(self, s: str) -> str:
        counter: dict[str, int] = {}
        for char in s:
            if not char in counter:
                counter[char] = 0
            counter[char] += 1

        freq: list[tuple[str, int]] = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return "".join([pair[0] * pair[1] for pair in freq])
