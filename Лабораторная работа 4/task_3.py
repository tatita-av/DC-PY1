def delete(list_, index=None):
    ...  # TODO реализовать функцию удаления элемента из списка по индексу
def delete(list_, index=None):
    if index == None:
        index = len(list_)
    if index == len(list_):
        new_list = list_[:index-1]
        return new_list
    new_list = list_[:index]
    new_list.extend(list_[index+1:])
    return new_list

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
