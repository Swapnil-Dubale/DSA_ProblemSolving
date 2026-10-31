class Solution:
    def firstRepeated(self, arr):
        # code here 
        seen = set()
        sol = -1
        for i in range(len(arr)-1, -1, -1):
            if arr[i] in seen:
                sol = i+1
            else:
                seen.add(arr[i])
        return sol

numArr = [1, 5, 3, 4, 3, 5, 6]
#expected output = 2 as secons element is first rpeating element

obj = Solution()

print(obj.firstRepeated(numArr))
