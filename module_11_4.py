# Задание:
# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).
#
#
# Пример работы:
# number_info = introspection_info(42)
# print(number_info)
#
# Вывод на консоль:
# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
#
# Рекомендуется создавать свой класс и объект для лучшего понимания


#Решение:

import inspect



def introspection_info(obj):
    info = {}

    info["type"] = type(obj).__name__

    info["module"] = inspect.getmodule(obj).__name__ if inspect.ismodule(obj) else None

    atributes = []
    methods = []

    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            atributes.append(attr)
        info["attributes"] = atributes
        info["methods"] = methods

    if isinstance(obj, (int, float, list, tuple, dict, str, bytes)):
        info["length"] = len(obj) if hasattr(obj, "__len__") else 'N/A'
    if isinstance(obj, (int, float)):
        info["is_integer"] = isinstance(obj, int)

    return info


number_info = introspection_info("Ivan")
number_info1 = introspection_info(42)
print(number_info)
print(number_info1)

class Introspection:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"

my_introspection = Introspection("Ivan")
object_info = introspection_info(my_introspection)
print(object_info)