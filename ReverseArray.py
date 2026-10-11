class ReverseArray:
    def reversedArraywithUsingEmptyArray(self, arr):
        reversedList = []
        arrlen = len(arr) -1
        for i in range (0,len(arr)):
            reversedList.append(arr[arrlen])
            arrlen-=1
        return(reversedList)

##### OR BELOW LOGIC IF SAME ARRAY NEED TO BE MODIFED WITHOUT USING ANOTHER ARRAY

    def reverseArrayModifyingSameArray(self, arr):
        # code here
        
        arrlen = len(arr) -1
        start = 0
            #reversedList.append(arr[arrlen])
        while (start < arrlen):
            #print("Comparing . . .")
            #print(arr)
            temp = arr[start]
            arr[start] = arr[arrlen]
            arr[arrlen] = temp
                
            arrlen -=1
            start +=1
        return arr

classobj = ReverseArray()
numArray = [1,2,3,4,5]
print("Reversed Array Using another array",classobj.reversedArraywithUsingEmptyArray(numArray))
print("Reversed Array Modifying same array", classobj.reverseArrayModifyingSameArray(numArray))
