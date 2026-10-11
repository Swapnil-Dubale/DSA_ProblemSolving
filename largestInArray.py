class LargestNumberInArray:
    def findLargestNumber(self, arr):
        sol = arr[0]
        for i in range(0, len(arr)):
            #print("Comparing", arr[i], "with sol variable . . .")
            if arr[i] > sol:
                sol = arr[i]
        return sol

obj = LargestNumberInArray()
numberList = (1,2,3,4,5,99,6,7,-100,8,9,10,500)
#numberList = (-1,-100,-5,-50)
print(obj.findLargestNumber(numberList))
                
