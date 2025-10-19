class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or numRows < 2 or len(s) < numRows:
            return s 
        s = deque(list(s))
        result = ['']* numRows
        result[0] += s.popleft()
        while s: 
            for i in range(1, numRows):
                if s:result[i] += s.popleft()
            for i in range(numRows-2,-1,-1):
                if s: result[i] += s.popleft()
        return ''.join(result)