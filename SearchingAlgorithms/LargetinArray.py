def findLargestNumber(arr):
    max = arr[0]
    for i in range(0,len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

if __name__ == '__main__':
    numbers = [4,1,3,6,1]
    print(findLargestNumber(numbers))
