class Solution:
    def reverseBits(self, n: int) -> int:
        
        
        n = "{0:b}".format(n)
        n = n[::-1]
        for i in range(0, 32 - len(n)):
            n += '0'
        return int(n, 2)

f = Solution()   
print(f.reverseBits(23))