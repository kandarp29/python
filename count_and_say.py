class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = '1'
        
        if n == 1:
            return string
        else:
            c = ''
            for i in range(1,n-1):
                #count = 0
                i = str(i)
                a = string.count(i)
                a = str(a)
                b = a + i + c
            
        return b         
