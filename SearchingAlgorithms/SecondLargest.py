def findSecondLargestNumber(arr):
    max = -1
    for i in range(0,len(arr)):
        if arr[i] > max:
            max = arr[i]
    print("Max number", max)
    secondmax = -1
    
    for j in range(0,len(arr)):
        if  arr[j] > secondmax and arr[j] != max :
            secondmax = arr[j]
    print("secondmax Number")
    return secondmax

if __name__ == '__main__':
    numbers = [4,3,7,2,9,11,5,8]
    print(findSecondLargestNumber(numbers))
