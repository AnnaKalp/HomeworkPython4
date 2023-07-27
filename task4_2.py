"""Напишите функцию принимающую на вход только ключевые параметры и
возвращающую словарь, где ключ — значение переданного аргумента,
 а значение — имя аргумента. Если ключ не хешируем, используйте его
  строковое представление."""


def dict_from_kwargs(**kwargs):
    result_dict = {}

    for key, value in kwargs.items():
        try:
            result_dict[value] = key
        except:
            result_dict[str(value)] = key
    return result_dict


result = dict_from_kwargs(number=155, season="summer", a=[1, 2, 3], b={}, cat="Oscar")
print(result)
