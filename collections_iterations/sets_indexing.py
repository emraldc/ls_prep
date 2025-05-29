#Sets can't be indexed. Meaning you an't access alements 
# in a string using numerical indices (like you would 
# lists, tuples, or strings)

my_list = [10, 20 , 30]

print(my_list[0])
print(my_list[1])

# However, sets don't support this type of access

print('Example when trying to use indexing with sets')
my_set = {10, 20 ,30}

print(my_set[0])