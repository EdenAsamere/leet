class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        output=[first]
        for i in encoded:
            output.append(first^i)
            first ^= i
        return output
        