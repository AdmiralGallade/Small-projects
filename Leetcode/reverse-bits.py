# Reverse bits of a given 32 bits unsigned integer.

# Note:

# Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.


class Solution:
    def reverseBits(self, n: int) -> int:
        reversed= [int(x) for x in str(n)]
        reversed= reversed[::-1]

        reversed= str("".join(map(str,reversed)))
        print(reversed+'\n')
        #return reversed
        return int(reversed,2)

t=int(1001100)
n= Solution()
print(n.reverseBits(t))