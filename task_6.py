list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_i = 0
for i in range(len(list_numbers)):
    if (list_numbers[i] > list_numbers[max_i]):
        max_i = i
list_numbers[max_i],list_numbers[len(list_numbers)-1] = list_numbers[len(list_numbers)-1],list_numbers[max_i]
print(list_numbers)
