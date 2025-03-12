#User function Template for python3

class Solution:
    def primeDivision(self, n):
        # code here
        def sieve(n):
            isPrime = [True] * (n + 1)
            isPrime[0] = isPrime[1] = False
            for i in range(2, int(n**0.5) + 1):
                if isPrime[i]:
                    for j in range(i * i, n + 1, i):
                        isPrime[j] = False
            return isPrime
        isPrime = sieve(n)
        for i in range(2, n // 2 + 1):
            if isPrime[i] and isPrime[n - i]:
                return [i, n - i]
        return []


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        p1, p2 = ob.primeDivision(N)
        print(p1, end=" ")
        print(p2)

        print("~")
# } Driver Code Ends