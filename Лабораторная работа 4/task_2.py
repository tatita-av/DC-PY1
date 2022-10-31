def get_count_char(str_):
    str_ = str_.lower()
    dictionary = {}
    for word in str_:
        if word.isalpha() and not word in dictionary.keys():
            dictionary[word] = str_.count(word)
    return dictionary


def second_def(dict_):
    new_dict = {}
    sum_val = sum(dict_.values())
    for i in dict_:
        new_dict[i] = dict_[i] / sum_val * 100
    return new_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
dict_ = get_count_char(main_str)
new_dict = second_def(dict_)
print(dict_)
#print(new_dict)
