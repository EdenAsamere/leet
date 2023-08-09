class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        output=[first]
        for i in encoded:
            first, output = first^i, output + [first^i]
        return output
