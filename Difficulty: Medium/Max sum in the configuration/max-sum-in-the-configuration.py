#User function Template for python3

class Solution:
    def maxSum(self, arr): 
        # Code here
        n = len(arr)
        arrSum = sum(arr)
        S = sum(i * arr[i] for i in range(n))  # Initial sum S(0)
        maxS = S  # Store maximum found

        for i in range(1, n):  # Compute new sums for rotations
            S = S + arrSum - n * arr[n - i]  
            maxS = max(maxS, S)

        return maxS


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.maxSum(arr))
        print("~")
        T -= 1

# } Driver Code Ends