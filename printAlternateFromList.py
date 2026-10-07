numberList = [1,2,3,4,5,6,7,8,9,10]
AlternateNumberList = []
#print(len(numberList))
for i in range(0,len(numberList)):
    #print("Index : ",i, "Value : ",numberList[i])
    #print("Value : ",numberList[i])
    if(i%2 == 0):
        #print(numberList[i])
        #print("Index : ",i, "Value : ",numberList[i])
        AlternateNumberList.append(numberList[i])
print("Numbers from List Are . . .")
print(numberList)

print("Alternate Numbers from List Are . . .")
print(AlternateNumberList)
