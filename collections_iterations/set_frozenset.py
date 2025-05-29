letters = {'a', 'b', 'c'}
letters.add('a')
print(letters)

frozen_letters = frozenset(letters)
frozen_letters.add('e')