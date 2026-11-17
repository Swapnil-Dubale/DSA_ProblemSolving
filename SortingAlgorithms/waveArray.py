'''Given an sorted array arr[] of integers. Sort the array into a wave-like array (In Place). In other words, arrange the elements into a sequence such that : arr[0] ≥ arr[1] ≤ arr[2] ≥ arr[3] ≤ arr[4] ≥ ... and so on. If there are multiple solutions, find the lexicographically smallest one.

Note: The given array is sorted in ascending order, and modify the given array in-place without returning a new array.

Examples:

Input: arr[] = [1, 2, 3, 4, 5]
Output: [2, 1, 4, 3, 5]
Explanation: Array elements after sorting it in the waveform are 2, 1, 4, 3, 5.'''

class Solution:
    def sortInWave(self, arr):
        # code here
        if len(arr) == 1:
            return arr
        else:
            for i in range(0,len(arr)-1):
                if i%2==0:
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp
                
            return arr
obj = Solution()
array = [1,2,3,4,5]
waveArray = obj.sortInWave(array)
print("Wave Array : ",waveArray)