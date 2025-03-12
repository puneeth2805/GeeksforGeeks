#User function Template for python3
import math
class Solution:
    def largestPrimeFactor(self, n):
        res = []
        while n % 2 == 0:
            res.append(2)
            n //= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                res.append(i)
                n //= i
        if n > 2:
            res.append(n)
        
        return res[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.largestPrimeFactor(N))
        print("~")

# } Driver Code Ends