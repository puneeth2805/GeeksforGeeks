#User function Template for python3

class Solution:
    def isLucky(self, n): 
        #RETURN True OR False
        step = 2  # First elimination step
        while n >= step:
            if n % step == 0:  # If eliminated, return 0
                return 0
            n -= n // step  # Adjust N’s position
            step += 1  # Move to the next elimination step
        return 1  # If survived, it's lucky


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        obj = Solution()
        if obj.isLucky(n):
            print(1)
        else:
            print(0)
        
        print("~")
# } Driver Code Ends