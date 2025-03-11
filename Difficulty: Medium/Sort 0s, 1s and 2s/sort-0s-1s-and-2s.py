#{ 
 # Driver Code Starts

# } Driver Code Ends

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        lst=[0]*len(arr)
        k=0
        for i in range(len(arr)):
            if arr[i]==0:
                lst[k]=0
                k+=1
        for i in range(len(arr)):
            if arr[i]==1:
                lst[k]=1
                k+=1
        for i in range(len(arr)):
            if arr[i]==2:
                lst[k]=2
                k+=1
        for i in range(len(arr)):
            arr[i]=lst[i]
        


#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array
        print("~")
        
if __name__ == "__main__":
    main()

# } Driver Code Ends