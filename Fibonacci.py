sum_fibonacci = 0
num1 = 1
num2 = 2
fibonacci_total = 0
fibonacci_list = [1,2]
even_num = [0,2,4,6,8]

while num2 < 4000000:
    fibonacci_total = num1 + num2
    num1 = num2
    num2 = fibonacci_total
    fibonacci_list.append(num2)

for num in fibonacci_list:
    if num%2 == 0:
        sum_fibonacci += num

    # str_num = str(num)
    # for i in even_num:
    #     if str_num[-1] == str(i):
    #         sum_fibonacci += num
            #print(num)


print(fibonacci_total)
#print(fibonacci_list)
print(sum_fibonacci)
