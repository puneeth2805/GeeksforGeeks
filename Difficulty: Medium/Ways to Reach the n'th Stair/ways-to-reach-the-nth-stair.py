
class Solution:
    def countWays(self, n):
        # code here
        if n==1:
            return 1
        if n==2:
            return 2
            
        lst=[0]*(n+1)
        lst[1]=1
        lst[2]=2
        for i in range(3,n+1):
            lst[i]=lst[i-1]+lst[i-2]
        return lst[n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob = Solution()
        print(ob.countWays(m))

        print("~")

# } Driver Code Ends