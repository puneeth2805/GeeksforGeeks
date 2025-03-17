#User function Template for python3

class Solution:
    def reverse_exponentiation(self, n):
        MOD = 10**9 + 7  
        R = int(str(n)[::-1]) 
        return pow(n, R, MOD)
        

#{ 
 # Driver Code Starts
# Input handling
if __name__ == "__main__":
    T = int(input())  # test cases

    for _ in range(T):
        n = int(input())  # input N
        solution = Solution()
        ans = solution.reverse_exponentiation(n)
        print(ans)

# } Driver Code Ends