'''List practice
1. Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2. Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
3. Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
4. Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
5. Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке
этого элемента не было.
'''

import copy


# 1
lst = [lst1 + lst2 for lst1 in 'ab' for lst2 in 'bcd']
print(lst)

# 2
lst3 = slice(0, 6, 2)
print(lst[lst3])

# 3
lst4 = [lst5 + lst6 for lst5 in '1234' for lst6 in 'a']
print(lst4)

# 4
print(lst4.pop(1))

# 5
lst7 = copy.copy(lst4)
lst7.insert(1, '2a')
print(lst7)