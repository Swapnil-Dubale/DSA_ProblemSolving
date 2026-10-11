class Solution:
    def search(self, arr, x):
        # 
        for i in range(0,len(arr)):
            if(arr[i] == x):
                print(x,"Found at Index",arr[i])
                return x
        print(x, "Not Found in the List . . .")

NumbersList = [1,2,3,4,5,6,7,8,9,10]
numberToSearch = 11
sol = Solution()
sol.search(NumbersList, numberToSearch)
    #search(self, NumbersList, numberToSearch)