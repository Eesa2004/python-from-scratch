def bubble_sort(data):
    if len(data)> 1:
        for j in range(0, len(data)-1):
            for i in range(0, len(data)-j-1):
                if data[i] > data[i+1]:
                    data[i], data[i+1] = data[i+1], data[i]

                    
    else:
        print("list is too small")

    return data


num_list = [9, 3, 8, 2, 5, 6]
print(bubble_sort(num_list))

        
        
