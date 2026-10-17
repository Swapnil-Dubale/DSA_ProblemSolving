""" Binary Search  O(log n) Time and O(1) Space
It works on sorted arrays by repeatedly dividing the search interval in half. 
If the target matches the middle element, return it; otherwise, continue searching left or right."""

def BinarySearch(arr, low, high, x):
    if high >= low:
       # print("start with searching")
        mid = low + (high - low) // 2
        #print("Mid : ", mid)
        if (arr[mid] == x):
            return mid
        elif x < arr[mid]:
            return BinarySearch(arr, low, mid-1, x)

        elif x > arr[mid]:
            return BinarySearch(arr, mid+1, high, x)
        else:
            print("some logic messed up . . .")
    else:
        return -1

if __name__ == "__main__":
    numArray = [10,20,30,40,50,60,70,80,90,100]
    number = 50
    result = BinarySearch(numArray, 0, len(numArray), number)
    if result == -1:
        print("Element Not found in array")
    else:
        print("Element found in array at index : ", result)
