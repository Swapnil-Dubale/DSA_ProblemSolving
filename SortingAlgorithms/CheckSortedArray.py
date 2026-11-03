#Given an array arr[], check whether it is sorted in non-decreasing order. 
#Return true if it is sorted otherwise false.
'''
Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted.
Input: arr[] = [90, 80, 100, 70, 40, 30]
Output: false
Explanation: The given array is not sorted. '''

class ArrayOp:
    def checkAortedArray(self, arr):
        flag = "true"
        for i in range(1,len(arr)):
            if arr[i-1] < arr[i]:
                continue
            else:
                flag = "false"
                break
        return flag

obj = ArrayOp()
arr = [90, 80, 100, 70, 40, 30]
print(obj.checkAortedArray(arr))