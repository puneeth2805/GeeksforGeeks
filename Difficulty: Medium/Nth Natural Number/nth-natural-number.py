#User function Template for python3

class Solution:
    def findNth(self,n):
        #code here
        result = 0
        base = 1 
        
        while n > 0:
            result += (n % 9) * base
            n //= 9
            base *= 10  
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)
    print("~")

# } Driver Code Ends