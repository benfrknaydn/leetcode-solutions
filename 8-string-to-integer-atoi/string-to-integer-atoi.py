class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = re.search("^\s*([-+])?[0-9]+", s)
        return max(min(int(m.group(0)), 2147483647), -2147483648) if m else 0

