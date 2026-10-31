class Solution:
    def firstRepeated(self, arr):
        # code here 
        arrMid = len(arr)//2
        for i in range(0,arrMid):
            for j in range(i+1,len(arr)):
                if arr[i] == arr[j]:
                    return arr[i]
        return -1


obj = Solution()

numArray = [1, 5, 3, 4, 3, 5, 6]
#numArray = [1, 2, 3, 4]
print(obj.firstRepeated(numArray))
