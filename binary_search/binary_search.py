def binary_search(data, x):
    lb = 0
    ub = len(data)-1
    found = False

    if x in data:
        while found == False:
            if len(data) > 1:
                mp = round((lb+ub)/2)
                
                if x == data[mp]:
                    found = True
                    
                elif x < data[mp] and x >= data[lb]:
                    ub = mp-1

                elif x > data[mp] and x <= data[ub]:
                    lb = mp+1
                    
        if found == True:
            print(x, "is in index position:", mp)
            return''

    else:
        (print(x, 'is out of range'))
        return''


    

numList = [1,2,3,4,5,6,7,8,9]
print(binary_search(numList, 9))
