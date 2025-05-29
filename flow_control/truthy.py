# value = 5
# if value:
#     print(f'{value} is truthy')
# else:
#     print(f'{value} is falsy')

foo = None
bar = 'qux'

if foo or bar:
    is_ok = True
else:
    is_ok = False