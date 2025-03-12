#User function Template for python3
import math
class Solution:
    def sieveOfEratosthenes(self, n):
        if n < 2:
            return [] 

        isPrime = [True] * (n + 1)  
        isPrime[0] = isPrime[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
            if isPrime[i]:
                for j in range(i * i, n + 1, i):
                    isPrime[j] = False
        primes = [i for i in range(n + 1) if isPrime[i]]
        return primes
    	


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(n)
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends