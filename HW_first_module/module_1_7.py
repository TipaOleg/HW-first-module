immutable_var = (1, 'qwerty', True, [1, 2, 3], 151.951)
print(immutable_var)
# immutable_var[1] = 22
# Кортеж не может быть назначен значением во второй раз, что делает его "read-only" списком, то есть значения внури кортежа неизменяемы, и назначаются единожды
mutable_list = [1, 2, 3, 4, 5]
mutable_list[0] = 666
print(mutable_list)