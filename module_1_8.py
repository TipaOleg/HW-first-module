my_dict = {'q':1, 'w':2, 'e':3, 'r':4}
print(my_dict)
print(my_dict['q'], my_dict.get('u'))
my_dict.update({'t':5,
                'y':6})
last_key = my_dict.pop('w')
print(last_key)
print(my_dict)

my_set = {1, 2, 3, 4, 5, 15454, 3, 4687, 1, 5}
print(my_set)
my_set.update({6, 7})
my_set.discard(15454)
print(my_set)