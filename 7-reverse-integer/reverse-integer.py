class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result= int(''.join(reversed(str(abs(x))))) * ( -1 if x < 0 else 1)
        return result if 2147483648 > result > -2147483649 else 0