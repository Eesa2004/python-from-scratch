count = 0
count_list = []
biggest = 0
x = 0
duplicate = 0
input_list = []
user_input = input("Please Enter any string: ")

for i in user_input:
    for x in user_input:
        if i == x:
            count_list.append(count)
            count = 0
        else:
            count += 1

for i in count_list:
    if i > biggest:
        biggest = i

print(f"Longest substring is: {biggest}")
