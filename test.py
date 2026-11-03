for i in range(0, 5):
    print(i)


        flag = "true"
        for i in range(0, len(arr)-1):
            if i == 0:
                pass
            elif arr[i] < arr[i-1]:
                return False
        return True