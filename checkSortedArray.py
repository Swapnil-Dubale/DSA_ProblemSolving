#Input: arr[] = [10, 20, 30, 40, 50]
#Output: true
#Explanation: The given array is sorted.

#Input: arr[] = [90, 80, 100, 70, 40, 30]
#Output: false
#Explanation: The given array is not sorted.

class checkSortedArray:
    def sortedArrayCheck(self, arr):
        flag = "true"
        for i in range(0, len(arr)):
            if i == 0:
                pass
            elif arr[i] < arr[i-1]:
                return False
        return True

sortedArray = [10, 20, 30, 40, 50]
unSortedArray = [90, 80, 100, 70, 40, 30]
obj = checkSortedArray()
print(obj.sortedArrayCheck(sortedArray))
print(obj.sortedArrayCheck(unSortedArray))