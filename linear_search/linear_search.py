def linear_search(data, x):
    if len(data) > 1:
        for i in range(0, len(data)-1):
            if data[i] == x:
                print(x, "is in index position", i)
                return''
        else:
            print(x, "is not in the list")
            return ''
num_list = [3,2,6,5,4,67,6,54,6,8,43,5,78,7,643,1,32,4,33,5,7,765,4,5,8,9,7]
print(linear_search(num_list, 5))
