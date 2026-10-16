#Linear Search : O(n) Time and O(1) Space
#It is the simplest searching algorithm that checks each element sequentially until the key is found 
# or the collection is fully traversed. Works on both sorted and unsorted data.

def linearSearch(arr, x):
    for i in range(0, len(arr)):
        if arr[i] == x:
            return i
        #elif(i == len(arr) -1):
        #    return -1
    return -1
if __name__ == "__main__":
    numArr = [10, 20, 30, 40, 50, 60]
    numberToFind = 60
    result = linearSearch(numArr, numberToFind)
    #print(result)
    if (result == -1):
        print("Element not present in array")
    else:
        print("Element found in array at index ", result)
