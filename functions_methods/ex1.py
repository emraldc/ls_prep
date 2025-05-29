foo = 'strawberry'

def set_foo():
    foo = 'bar'
    print(foo) # only has access to inside the function scope

set_foo()
print(foo)  # only has access outside of the function scopeß