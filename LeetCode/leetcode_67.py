class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = "0b" + a
        b = "0b" + b
        a = int(a, 2)
        b = int(b, 2)
        result = bin(a + b)
        result = result[2:]
        return result