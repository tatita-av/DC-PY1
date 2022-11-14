from random import randint

def get_unique_list_numbers() -> list[int]:
    dt = []
    for i in range(15):
        a = randint(-10, 10)
        while a in dt:
            a = randint(-10, 10)
        dt.append(a)
    return dt


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
