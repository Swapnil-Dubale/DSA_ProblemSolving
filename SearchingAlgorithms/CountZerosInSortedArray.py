#Given an array arr of only 0's and 1's. The array is sorted in such a manner that all the 1's are placed first and then they are followed by all the 0's.
#Find the count of all the 0's.
#Input: arr[] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
#Output: 3
#Explanation: There are 3 0's in the given array.

class Solution:
    def countZeroes(self, arr):
        # code here
        sum = 0
        total = len(arr)
        for i in range(0,len(arr)):
            if arr[i] == 0:
                sum = total - i
                return sum

obj = Solution()
numbers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
print("The Number of Zero's is")
print(obj.countZeroes(numbers))
