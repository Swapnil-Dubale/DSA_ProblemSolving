def findSecondLargestbySort(arr):
    arr.sort()
    max = arr[-1]
    secondMax = arr[-2]
    print("Max Number", max)
    print("Second Max Number",secondMax)

if __name__ == '__main__':
    numbers = [2,5,3,7,9,3]
    findSecondLargestbySort(numbers)
