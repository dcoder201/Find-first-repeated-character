#User function Template for python3

class Solution:

    def firstRepChar(self, s):
        # code here
        l=[]

        for i in range(len(s)):

            if s[i] not in l:

                l.append(s[i])

            else:

                n=len(l)

                k=s[len(l)]

                return k

        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.firstRepChar(s))
# } Driver Code Ends
